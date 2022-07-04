def main(tl_text,dl_text,ll_text,fl_text):
    file1 = open("projects.txt", "a")  # write mode
    L = [
        "{0} with {1} lines and {2} files. Made on {3}\n".format(tl_text, ll_text, fl_text, dl_text),
    ]
    for i in L:
        file1.write(i)
    file1.close()