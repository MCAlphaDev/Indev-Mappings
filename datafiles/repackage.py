import sys, re

def default_indexfn(x):
    ord_ = ord(x.swapcase()) - 65
def repackage(tiny, obfregex="", indexFn=lambda x : ord(x)-97):
    matcher = (lambda x : False) if obfregex == "" else (lambda x : re.match(obfregex, x) is not None)
    result = ""
    for line in tiny.split("\n"):
        line = line.strip() # in case of weird whitespace
        
        if line == "" or line[0] == '#' or line.endswith("intermediary"): # ignore this stuff
            result += line + "\n"
        else:
            tokens = line.split("\t", 3)

            if tokens[0] == "CLASS" and tokens[2].startswith("net/minecraft/"): # only classes in net/minecraft intermediary
                # only new (not run through this before)
                # this should be safe as if it runs twice while matching this it will generate the same output anyway
                if re.search(r"pkg[0-9]+\/", tokens[2]) is None:
                    packages = tokens[1].split("/")
                    clazz = tokens[2].split("/")[-1]
                    new_line = "CLASS\t"
                    new_line += tokens[1] + "\t"

                    # add packages
                    for package in packages[:-1]:
                        if matcher(package):
                            print(package)
                            new_line += "pkg" + str(indexFn(package)) + "/"
                        else:
                            new_line += package + "/" # just the package
                    new_line += clazz + "\n"
                    print(new_line)
                else:
                    result += line + "\n"
            else:
                result += line + "\n"
    return result
        

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python repackage.py <intermediaries>")
    else:
        with open(sys.argv[1], 'r') as file:
            contents = file.read()
        
        repackage(contents, r"[A-z]$")
