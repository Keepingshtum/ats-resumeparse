import text_process

# Python program for KMP Algorithm 
def KMPSearch(pat, txt): 
    M = len(pat) 
    N = len(txt) 
    found = 0
  
    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*M 
    j = 0 # index for pat[] 
  
    # Preprocess the pattern (calculate lps[] array) 
    computeLPSArray(pat, M, lps) 
  
    i = 0 # index for txt[] 
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            # print("Found pattern at index ", str(i-j))
            found = found+1
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return found, pat
  
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step. 
            if len != 0: 
                len = lps[len-1] 
  
                # Also, note that we do not increment i here 
            else: 
                lps[i] = 0
                i += 1
  
# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"

Job_description = "python, pyspark, oracle, angular, linux, azure"
# 
# 'Machine Learning, Supervised Learning, Unsupervised Learning, Regression techniques, Classification'
# 'PHP, Mysql, Flask, Machine Learning, Java'
# 'SAP, Hadoop, ERP, ABAP, JAVA'

resumetxt = text_process.extractdoctext()

# "sandeep sandeepv gmailcom nine hundred and eighteen billion, eight hundred and ninety-seven million, two hundred and forty-nine thousand, six hundred and forty-nin hyderabad profess sum around elev year expery technolog lead dat sci dat sci three year relev expery dat sci cre work model good pract knowledg diff superv unsuperv learn techn parametricnonparamet algorithm support vect machin kernel clust dimend reduc pca lda good knowledg understand diff regress class clust techn extend expery import cle manip summ dat build machin learn regress model dat pipelin expery skil panda numpy matplotlib scikitlearn load manip analys vis dat set us python work jupyt notebook spyd id googl colab expery machin learn algorithm log regress knn svm random forest linear regress kme clust decid tre random forest deep reinforc learn evalu model us cross valid log loss funct roc curv us auc feat select excel commun skil success work fastpac multitask environ independ collab team selfmot enthusiast learn microsoft net eight year expery analys design develop cli serv web bas nti apply us net technolog c aspnet aspnet mvc adonet wcf window serv sql serv twenty million, eighty-two thousand and twelve jav script jquery act involv softw develop impl maint apply us agil methodolog proficy develop serv us web serv wcf aspnet web ap technolog expery valid us soapu postm tool splunk us capturingsearch log web serv good troubleshoot techn glitch perform cod review strong understand net framework clr jit oop knowledg design pattern dec fact adapt good work knowledg sql query stor proc join index trig join design tabl us sql serv two hundred thousand, eight hundred and twelve funct domain expery involv healthc brok project man techn skil net technolog c net two thousand and thirty-five aspnet two thousand and thirty-five linq adonet web serv wcf webap aspnet mvc40 expery script jav script jquery work tool lik splunk soap ui post man fog light strong object program langu skil heal car fin domain expery program databas python c net web ap orac sql serv id cod vert jupyt notebook spid vis studio tfs svn github technolog c net two thousand and thirty-five aspnet two thousand and thirty-five linq adonet web serv wcf web ap aspnet mvc40 framework net framework two hundred and three thousand, five hundred and forty frontend tool microsoft vis studio net two hundred billion, five hundred and twenty million, eighty-two thousand and ten tool soapu splunk foglight apm rdbms sql serv two hundred billion, five hundred and twenty million, eighty-two thousand and twelve script langu jav script jquery config tool vss sixty tfs report serv ssrs twenty million, fifty-two thousand and eight educ bachel educ indust engin man bms colleg engin bang ind two thousand and ten two thousand and fourteen preunivers educ phys chem mathem electron shri bhagaw mahav jain colleg two thousand and eight two thousand and ten profess expery kansastek https wwwkansastekcom aug two thousand and nineteen pres web develop project kansastek usbas startup company develop innov platform recruit autom way tak techn interview evalu us art intellig respons us expery design impl evalu mod web apply collect analys dat interview evalu dat convert result vis repres form chart graph display report card interview design develop cod edit mod web apply let interview candid tak cod challeng six diff program langu jav javascrib python sql c c autom evalu realtim integr cod edit syntax highlight cod assist determin op feas scal produc follow high cod standard prop design docu maintain feat research recommend op sourc technolog monaco edit quil richtext edit chart compilerun nod plugin carry project develop task reduc develop effort drast valid thorough diff test cas cov feat ens apply bug fre provid assist suggest idea feedback peer man technolog angul eight nod twelv angul mat design typescrib javascrib css html mongodb mongooses express gitlab googl cloud tat consult serv https wwwtcscom jun two thousand and fourteen sep two thousand and eighteen system engin assocy system engin four year project1 sep two thousand and seventeen sep two thousand and eighteen multin retail company bas duba requir intern monit tool web apply monit one thousand stor sev diff country monit analys many busy paramet workflow dat back off stor cent off respons us expery design develop dashboard pag bas custom spec develop rest ap jav retriev liv dat multipl databas multipl stor serv cent serv complet impl dashboard mod us dat ap analys paramet one thousand stor display singl pag interact dashboard multipl chart graph bet vis repres us chart libr uplift us interfac bootstrap websit templ ident area mod improv perform sql query ens optim perform maintain cod standard qual technolog angul javascrib css html5 bootstrap orac db sql jav sev project2 apr two thousand and seventeen sep two thousand and seventeen multin telecommun hold group requir intern web apply track monit facilit onlin transport supply chain process company distribut wareh superv stor room superv ship superv const upd ord delivery process five hundred produc via web apply respons develop rest ap jav custom ord mod pick pack ship mod writ sql query diff typ custom ord ord detail pack ship detail us expery design develop pick pack ship workflow employ record act detail web apply subsequ act unlock employ op ens break workflow produc thorough valid test ap technolog angul javascrib css html5 bootstrap jav sev orac db sql gitlab apach tomc project3 jun two thousand and sixteen apr two thousand and seventeen web apply streamline grant man process record detail onlin intend us stakehold gen grant man process nongovern org respons us interfac design develop interact dashboard vert tre view flow entir process approv evalu could ad input develop ap jav backend workflow entir process start propos submit project fund alloc multipl level approv perform evalu workflow report monit writ sql query desk evalu onsit evalu compon research recommend activit workflow engin help reduc develop effort complex drast integr activit workflow engin ap jav ap integr angul apply jav ap technolog angulars jav sev bootstrap javascrib html5 css sql activit workflow engin apach http serv apach tomc serv gitlab project4 sep two thousand and fourteen apr two thousand and sixteen web apply bhar rur liv find set govern ind intend tim transp monit evalu project along facilit partn reg propos apply process support un innov project civil socy sect respons gath refin spec requir bas techn nee propos process web apply develop propos process apply involv fifty input field dat ent reg partn php develop workflow two level approv process propos php develop monit tool apply track fin detail project us bootstrap jquery develop word count feat two hundred input text field throughout apply us jquery writ sql query fetch insert upd detail propos fin detail cre maintain man us web apply cre maintain docu feat web apply technolog php fiv bootstrap jquery javascrib html css mysql phpmyadmin apach http serv gitlab pass merit profess chess play multipl competit plac 2nd karnatak stat level competit hold niit plac top ten district level school competit mathem sci two on"
# "machin learn superv learn unsuperv learn regress techn class"

maintxt = text_process.processtext(resumetxt)

searchwords = Job_description.split(',')

patern = []

for w in searchwords:
    patern.append(text_process.processtext(w, 'skip'))
# print(patern)

#construct dictionary of search words
res = {patern[i]: searchwords[i].strip() for i in range(len(searchwords))} 
print(str(res))

count = 0
txtfound = []

for p in patern:
    c, wrd = KMPSearch(p, maintxt) 
    if c > 0:
        txtfound.append(res.get(wrd))
        count+=1

print('Search text: ')        
print(Job_description)
print('words found: ', txtfound)

# print('pattern', str(len(patern.split(' '))))
cal = count/len(patern)
print(cal)


