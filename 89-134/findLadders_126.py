class Solution:
    def findLadders_126(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)  # 转换为hash实现O(1)的in判断
        if endWord not in wordList:
            return []
        # 分别为答案、用于剪枝的已访问哈希，前向分支和后向分支，当前的前向分支以及后向分支中的路径和的长度
        # 前向路径分支与后向路径分支的字典结构为{结束词：到达该结束词的路径列表}
        res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):  # 始终从路径分支较少的一端做BFS
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i] + a + word[i + 1:]  # 对结束词尝试每一位的置换
                        if new in backward:  # 如果在后向分支列表里发现置换后的词，则路径会和
                            if paths[0][0] == beginWord:  # 前向分支是从beginWord开始的，添加路径会和的笛卡尔积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:  # 后向分支是从endWord开始的，添加路径会和的笛卡尔积
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in wordList and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break
            forward = tmp  # 更新前向分支
        return res


def main():
    beginWord = "cet"
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes",
                "ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit",
                "rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut",
                "sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu",
                "ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew",
                "ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan",
                "map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi",
                "sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib",
                "mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum",
                "pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag",
                "hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop",
                "but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod",
                "hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat",
                "fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap",
                "can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey",
                "bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao",
                "mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat",
                "sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo",
                "hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit",
                "maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed",
                "vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew",
                "zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen",
                "oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop",
                "haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin",
                "mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun",
                "try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas",
                "zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue",
                "dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix",
                "cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup",
                "jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig",
                "fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant",
                "net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot",
                "del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah",
                "hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big",
                "ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met",
                "hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid",
                "god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her",
                "nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid",
                "mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug",
                "pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"
                ]
    endWord = "ism"

    a = Solution()
    print(a.findLadders_126(beginWord, endWord, wordList))


if __name__ == '__main__':
    main()
