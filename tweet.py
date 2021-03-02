# coding=utf-8

# importing the libraries
# the keys_for_faiz_bot and lyrics libraries are .py files

import os
from os import environ
import tweepy
import time
from random import *

# setting up the authentication framework

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']

key = environ['key']
secret = environ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# defining variables to be used afterwards

FILE_NAME = 'last_seen.txt'

lyrics = ['yuuñ bahār aaī hai is baar ki jaise qāsid \ kūcha-e-yār se be-nail-e-marām aatā hai ',
          'sham-e-nazar ḳhayāl ke anjum jigar ke daaġh \ jitne charāġh haiñ tirī mahfil se aae haiñ ',
          'kabhī kabhī yaad meñ ubharte haiñ naqsh-e-māzī miTe miTe se \ vo āzmāish dil o nazar kī vo qurbateñ sī vo fāsle se ',
          'aap ko chehre se bhī bīmār honā chāhiye \ ishq hai to ishq kā izhār honā chāhiye ',
          'dil kā har taar larzish-e-paiham \ jaañ kā har rishta vaqf-e-soz-o-gudāz ',
          'dekh aaeñ chalo kū-e-nigārāñ kā ḳharāba \ shāyad koī mahram mile vīrānī-e-dil kā ',
          'tum aa rahe ho ki bajtī haiñ merī zanjīreñ \ na jaane kyā mire dīvār-o-bām kahte haiñ ',
          'rāz-e-ulfat chhupā ke dekh liyā \ dil bahut kuchh jalā ke dekh liyā ',
          'hadīs-e-yār ke unvāñ nikharne lagte haiñ \ to har harīm meñ gesū sañvarne lagte haiñ ',
          'havas-e-mutrib-o-sāqī meñ pareshāñ akasr \ abr aatā hai kabhī māh-e-tamām aatā hai ',
          'shauq vāloñ kī hazīñ mahfil-e-shab meñ ab bhī \ āmad-e-subh kī sūrat tirā naam aatā hai ',
          'hasrat-e-dīd meñ guzarāñ haiñ zamāne kab se \ dasht-e-ummīd meñ gardāñ haiñ divāne kab se ',
          'phir nazar meñ phuul mahke dil meñ phir shameñ jalīñ \ phir tasavvur ne liyā us bazm meñ jaane kā naam ',
          'sharh-e-firāq madh-e-lab-e-mushkbū kareñ \ ġhurbat-kade meñ kis se tirī guftugū kareñ ',
          'vo jo ab chaak garebāñ bhī nahīñ karte haiñ \ dekhne vaalo kabhī un kā jigar to dekho ',
          'jis ḳhaak meñ mil kar ḳhaak hue vo surma-e-chashm-e-ḳhalq banī \ jis ḳhaar pe ham ne ḳhuuñ chhiḌkā ham-rañg-e-gul-e-tannāz kiyā ',
          'sabhī kuchh hai terā diyā huā sabhī rāhateñ sabhī kulfateñ \ kabhī sohbateñ kabhī furqateñ kabhī dūriyāñ kabhī qurbateñ ',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ',
          'jaane kyā vaza hai ab rasm-e-vafā kī ai dil \ vaz-e-derīna pe isrār karūñ yā na karūñ ',
          'shaiḳh sāhab se rasm-o-rāh na kī \ shukr hai zindagī tabāh na kī ',
          'har ik shab har ghaḌī guzre qayāmat yuuñ to hotā hai \ magar har subh ho roz-e-jazā aise nahīñ hotā ',
          'minnat-e-chāra-sāz kaun kare \ dard jab jāñ-navāz ho jaae ',
          'siine pe haath hai na nazar ko talāsh-e-bām \ dil saath de to aaj ġham-e-ārzū kareñ ',
          'husn se dil lagā ke hastī kī \ har ghaḌī ham ne ātishīñ kī hai ',
          'ham ne sab sher meñ sañvāre the \ ham se jitne suḳhan tumhāre the ', 'ho chukā ishq ab havas hī sahī ',
          'har ik qadam ajal thā har ik gaam zindagī \ ham ghuum phir ke kūcha-e-qātil se aae haiñ ',
          'ye ajab qayāmateñ haiñ tire rahguzar meñ guzarāñ \ na huā ki mar miTeñ ham na huā ki jī uTheñ ham ',
          'vo rañg hai imsāl gulistāñ kī fazā kā \ ojhal huī dīvār-e-qafas hadd-e-nazar se ',
          'yahāñ vābastagī vaañ barhamī kyā jāniye kyuuñ hai \ na ham apnī nazar samjhe na ham un kī adā samjhe ',
          'har samt pareshāñ tirī aamad ke qarīne \ dhoke diye kyā kyā hameñ bād-e-saharī ne ',
          'merī qismat se khelne vaale \ mujh ko qismat se be-ḳhabar kar de ',
          'sab qatl ho ke tere muqābil se aae haiñ \ ham log surḳh-rū haiñ ki manzil se aae haiñ ',
          'shaiḳh se be-hirās milte haiñ \ ham ne tauba abhī nahīñ kī hai ',
          'vo to vo hai tumheñ ho jāegī ulfat mujh se \ ik nazar tum mire mahbūb-e-nazar to dekho ',
          "kaun qātil bachā hai shahr meñ 'faiz' ",
          'josh-e-vahshat hai tishna-kām abhī \ chāk-e-dāman ko tā jigar kar de ',
          'ravāñ hai nabz-e-daurāñ gardishoñ meñ āsmāñ saare \ jo tum kahte ho sab kuchh ho chukā aise nahīñ hotā ',
          'tujhe pukārā hai be-irāda \ jo dil dukhā hai bahut ziyāda ',
          'ashk to kuchh bhī rañg lā na sake \ ḳhuuñ se tar aaj āstīñ kī hai ',
          'thī magar itnī rāegāñ bhī na thī \ aaj kuchh zindagī se kho baiThe ',
          'vo nazar baham na pahuñchī ki muhīt-e-husn karte \ tirī diid ke vasīle ḳhad-o-ḳhāl tak na pahuñche ',
          'vo ahd-e-ġham kī kāhish-hā-e-be-hāsil ko kyā samjhe \ jo un kī muḳhtasar rūdād bhī sabr-āzmā samjhe ',
          'mire chāra-gar ko naved ho saf-e-dushmanāñ ko ḳhabar karo \ jo vo qarz rakhte the jaan par vo hisāb aaj chukā diyā ',
          'āshob-e-nazar se kī ham ne chaman-ārāī \ jo shai bhī nazar aaī gul-rañg nazar aaī ',
          'pūchho to udhar tīr-fagan kaun hai yaaro \ sauñpā thā jise kaam nigahbānī-e-dil kā ',
          'jamegī kaise bisāt-e-yārāñ ki shīsha o jaam bujh gae haiñ \ sajegī kaise shab-e-nigārāñ ki dil sar-e-shām bujh gae haiñ ',
          'kab yaad meñ terā saath nahīñ kab haat meñ terā haat nahīñ \ sad-shukr ki apnī rātoñ meñ ab hijr kī koī raat nahīñ ',
          'kabhī to subh tire kunj-e-lab se ho āġhāz \ kabhī to shab sar-e-kākul se mushk-bār chale ',
          'der se aañkh pe utrā nahīñ ashkoñ kā azaab \ apne zimme hai tirā qarz na jaane kab se ',
          'sozish-e-dard-e-dil kise maalūm \ kaun jaane kisī ke ishq kā raaz ',
          "nahīñ ḳhauf-e-roz-e-siyah hameñ ki hai 'faiz' zarf-e-nigāh meñ ",
          'qarīb aa ai mah-e-shab-e-ġham nazar pe khultā nahīñ kuchh is dam \ ki dil pe kis kis kā naqsh baaqī hai kaun se naam bujh gae haiñ ',
          'dāman-e-dard ko gulzār banā rakkhā hai ',
          'chashm-e-maigūñ zarā idhar kar de \ dast-e-qudrat ko be-asar kar de ',
          'maidān-e-vafā darbār nahīñ yaañ nām-o-nasab kī pūchh kahāñ \ āshiq to kisī kā naam nahīñ kuchh ishq kisī kī zaat nahīñ ',
          'bahut girāñ hai ye aish-e-tanhā kahīñ subuk-tar kahīñ gavārā \ vo dard-e-pinhāñ ki saarī duniyā rafīq thī jis ke vāste se ',
          'chupke chupke raat din aañsū bahānā yaad hai \ ham ko ab tak āshiqī kā vo zamānā yaad hai ',
          'rañg-o-ḳhushbū ke husn-o-ḳhūbī ke \ tum se the jitne istiāre the ',
          'yaar āshnā nahīñ koī Takrāeñ kis se jaam \ kis dil-rubā ke naam pe ḳhālī subū kareñ ',
          'lo sunī gaī hamārī yuuñ phire haiñ din ki phir se ',
          'dil muddaī ke harf-e-malāmat se shaad hai \ ai jān-e-jāñ ye harf tirā naam hī to hai ',
          'the shab-e-hijr kaam aur bahut \ ham ne fikr-e-dil-e-tabāh na kī ',
          'ab junūñ had se baḌh chalā hai \ ab tabīat bahal chalī hai ',
          'na tan meñ ḳhuun farāham na ashk āñkhoñ meñ \ namāz-e-shauq to vājib hai be-vazū hī sahī ',

          'jaise ham-bazm haiñ phir yār-e-tarah-dār se ham \ raat milte rahe apne dar-o-dīvār se ham ',

          'sarḳhushī meñ yūñhī dil-shād o ġhazal-ḳhvāñ guzre \ kū-e-qātil se kabhī kūcha-e-dildār se ham ',
          'ishq dil meñ rahe to rusvā ho \ lab pe aae to raaz ho jaae ',
          'aur kyā dekhne ko baaqī hai \ aap se dil lagā ke dekh liyā ', 'lutf kā intizār kartā huuñ ',
          'sehn-e-gulshan meñ kabhī ai shah-e-shamshād-qadāñ \ phir nazar aae salīqa tirī raanāī kā ',
          'chāñd nikle kisī jānib tirī zebāī kā \ rañg badle kisī sūrat shab-e-tanhāī kā ',
          'baat bas se nikal chalī hai \ dil kī hālat sambhal chalī hai ',
          'qissa-e-sāzish-e-aġhyār kahūñ yā na kahūñ \ shikva-e-yār-e-tarah-dār karūñ yā na karūñ ',
          'kab tak sunegī raat kahāñ tak sunāeñ ham \ shikve-gile sab aaj tire rū-ba-rū kareñ ',
          'shafaq kī raakh meñ jal bujh gayā sitāra-e-shām \ shab-e-firāq ke gesū fazā meñ lahrāe ',
          'ham se be-bahra huī ab jaras-e-gul kī sadā \ varna vāqif the har ik rañg kī jhankār se ham ',
          'tumhārī har nazar se munsalik hai rishta-e-hastī \ magar ye duur kī bāteñ koī nādān kyā samjhe ',
          'tere dar tak pahuñch ke lauT aae \ ishq kī aabrū Dubo baiThe ',
          'har manzil-e-ġhurbat pe gumāñ hotā hai ghar kā \ bahlāyā hai har gaam bahut dar-ba-darī ne ',
          'ye zid hai yaad harīfān-e-bāda-paimā kī \ ki shab ko chāñd na nikle na din ko abr aae ',
          'nigāh o dil ko qarār kaisā nashāt o ġham meñ kamī kahāñ kī \ vo jab mile haiñ to un se har baar kī hai ulfat nae sire se ',
          "pahle bhī tavāf-e-sham-e-vafā thī rasm mohabbat vāloñ kī \ ham tum se pahle bhī yahāñ 'mansūr' hue 'farhād' hue ",
          'ham saada hī aise the kī yuuñ hī pazīrāī \ jis baar ḳhizāñ aaī samjhe ki bahār aaī ',
          'sabā se karte haiñ ġhurbat-nasīb zikr-e-vatan \ to chashm-e-subh meñ aañsū ubharne lagte haiñ ',
          'kisī tarah to jame bazm mai-kade vaalo \ nahīñ jo bāda-o-sāġhar to hāv-hū hī sahī ',
          'jahān-e-dil meñ kaam aatī haiñ tadbīreñ na taazīreñ \ yahāñ paimān-e-taslīm-o-razā aise nahīñ hotā ',
          'phir niklā hai dīvāna koī phūñk ke ghar ko \ kuchh kahtī hai har raah har ik rāhguzar se ',
          'kis shahr na shohra huā nādānī-e-dil kā \ kis par na khulā raaz pareshānī-e-dil kā ',

          'aise nādāñ bhī na the jaañ se guzarne vaale \ nāseho pand-garo rāhguzar to dekho ',
          'aahaT sī koī aae to lagtā hai ki tum ho \ saaya koī lahrāe to lagtā hai ki tum ho ',
          'ik pal meñ ik sadī kā mazā ham se pūchhiye \ do din kī zindagī kā mazā ham se pūchhiye ',
          'kabhī manzil kabhī raste ne hameñ saath diyā \ har qadam uljhe rahe qāfila-sālār se ham ',
          'ye jafā-e-ġham kā chāra vo najāt-e-dil kā aalam \ tirā husn dast-e-īsā tirī yaad rū-e-maryam ',
          'yaad kā phir koī darvāza khulā āḳhir-e-shab \ dil meñ bikhrī koī ḳhushbu-e-qabā āḳhir-e-shab ',
          'apne har har lafz kā ḳhud āīna ho jāūñgā \ us ko chhoTā kah ke maiñ kaise baḌā ho jāūñgā ',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ',
          'tere kūche meñ bādshāhī kī \ jab se nikle gadāgarī kī hai ',
          'lo vasl kī saaat aa pahuñchī phir hukm-e-huzūrī par ham ne \ āñkhoñ ke darīche band kiye aur siine kā dar baaz kiyā ',
          "'faiz' takmīl-e-ġham bhī ho na sakī ",
          'mai-ḳhāne meñ aajiz hue āzurda-dilī se \ masjid kā na rakkhā hameñ āshufta-sarī ne ',
          'shāḳh par ḳhūn-e-gul ravāñ hai vahī \ shoḳhī-e-rañg-e-gulsitāñ hai vahī ',
          'terī sūrat jo dil-nashīñ kī hai \ āshnā shakl har hasīñ kī hai ',
          'ab ke baras dastūr-e-sitam meñ kyā kyā baab īzād hue \ jo qātil the maqtūl hue jo said the ab sayyād hue ',
          'barq sau baar gir ke ḳhaak huī \ raunaq-e-ḳhāk-e-āshiyāñ hai vahī ',
          'vahī phir mujhe yaad aane lage haiñ \ jinheñ bhūlne meñ zamāne lage haiñ ',
          'tere qaul-o-qarār se pahle \ apne kuchh aur bhī sahāre the ',
          'nayā ik rishta paidā kyuuñ kareñ ham \ bichhaḌnā hai to jhagḌā kyuuñ kareñ ham ',
          "'faiz' auj-e-ḳhayāl se ham ne \ āsmāñ sindh kī zamīñ kī hai ", 'dil nā-umīd to nahīñ nākām hī to hai ',
          'bahār ab aa ke kyā karegī ki jin se thā jashn-e-rañg-o-naġhma \ vo gul sar-e-shāḳh jal gae haiñ vo dil tah-e-dām bujh gae haiñ ',
          'udhar ek harf ki kushtanī yahāñ laakh uzr thā guftanī \ jo kahā to sun ke uḌā diyā jo likhā to paḌh ke miTā diyā ',
          'yahī kanār-e-falak kā siyah-tarīñ gosha \ yahī hai matla-e-māh-e-tamām kahte haiñ ',
          'tujh ko dekhā to ser-chashm hue \ tujh ko chāhā to aur chaah na kī ',
          'saarī duniyā se duur ho jaae \ jo zarā tere paas ho baiThe ',
          'zikr-e-dozaḳh bayān-e-hūr o qusūr \ baat goyā yahīñ kahīñ kī hai ',
          'phir aag bhaḌakne lagī har sāz-e-tarab meñ \ phir shoale lapakne lage har dīda-e-tar se ',
          'sabā ne phir dar-e-zindāñ pe aa ke dī dastak \ sahar qarīb hai dil se kaho na ghabrāe ',
          'bahut sambhālā vafā kā paimāñ magar vo barsī hai ab ke barkhā \ har ek iqrār miT gayā hai tamām paiġhām bujh gae haiñ ',
          'karte haiñ jis pe taan koī jurm to nahīñ \ shauq-e-fuzūl o ulfat-e-nākām hī to hai ',
          'vahīñ haiñ dil ke qarāin tamām kahte haiñ \ vo ik ḳhalish ki jise terā naam kahte haiñ ',
          'fikr-e-dildāri-e-gulzār karūñ yā na karūñ \ zikr-e-murġhān-e-giraftār karūñ yā na karūñ ',
          'be-qarārī sī be-qarārī hai \ vasl hai aur firāq taarī hai ',
          'ijz-e-ahl-e-sitam kī baat karo \ ishq ke dam-qadam kī baat karo ',
          'chalo aao tum ko dikhāeñ ham jo bachā hai maqtal-e-shahr meñ \ ye mazār ahl-e-safā ke haiñ ye haiñ ahl-e-sidq kī turbateñ ',
          'ab bhī elān-e-sahar kartā huā mast koī \ dāġh-e-dil kar ke farozāñ sar-e-shām aatā hai ',
          'saf-e-zāhidāñ hai to be-yaqīñ saf-e-mai-kashāñ hai to be-talab \ na vo subh vird-o-vazū kī hai na vo shaam jām-o-subū kī hai ',
          'har haqīqat majāz ho jaae \ kāfiroñ kī namāz ho jaae ',
          'aaj un kī nazar meñ kuchh ham ne \ sab kī nazreñ bachā ke dekh liyā ',
          'koī pukāro ki ik umr hone aaī hai \ falak ko qāfila-e-roz-o-shām Thahrāe ',
          'phir harīf-e-bahār ho baiThe \ jaane kis kis ko aaj ro baiThe ',
          'har ajnabī hameñ mahram dikhāī detā hai \ jo ab bhī terī galī se guzarne lagte haiñ ',
          'tumhārī yaad ke jab zaḳhm bharne lagte haiñ \ kisī bahāne tumheñ yaad karne lagte haiñ ',
          'nahīñ nigāh meñ manzil to justujū hī sahī \ nahīñ visāl mayassar to aarzū hī sahī ',
          'gino sab hasrateñ jo ḳhuuñ huī haiñ tan ke maqtal meñ \ mire qātil hisāb-e-ḳhūñ-bahā aise nahīñ hotā ',
          'ab jahāñ mehrbāñ nahīñ koī \ kūcha-e-yār mehrbāñ hai vahī ', 'na gaī terī be-ruḳhī na gaī ',
          'be-hirs-o-havā be-ḳhauf-o-ḳhatar is haath pe sar is kaf pe jigar \ yuuñ kū-e-sanam meñ vaqt-e-safar nazzāra-e-bām-e-nāz kiyā ',
          'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī hai \ na karam hai ham pe habīb kā na nigāh ham pe adū kī hai ',
          'na ye ġham nayā na sitam nayā ki tirī jafā kā gilā kareñ \ ye nazar thī pahle bhī muztarib ye kasak to dil meñ kabhū kī hai ',
          'ye suḳhan jo ham ne raqam kiye ye haiñ sab varaq tirī yaad ke \ koī lamha subh-e-visāl kā koī shām-e-hijr kī muddateñ ',
          'vo tīrgī hai rah-e-butāñ meñ charāġh-e-ruḳh hai na sham-e-vāda \ kiran koī aarzū kī laao ki sab dar-o-bām bujh gae haiñ ',
          'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī \ na karam hai ham pe habīb kā na nigāh ham pe ',
          'pahle bhī ḳhizāñ meñ baaġh ujḌe par yuuñ nahīñ jaise ab ke baras \ saare buuTe patta patta ravish ravish barbād hue ',
          'dosto us chashm o lab kī kuchh kaho jis ke baġhair \ gulsitāñ kī baat rañgīñ hai na mai-ḳhāne kā naam ',
          'ham ne dil meñ sajā liye gulshan \ jab bahāroñ ne be-ruḳhī kī hai ',
          'sitam sikhlāegā rasm-e-vafā aise nahīñ hotā \ sanam dikhlāeñge rāh-e-ḳhudā aise nahīñ hotā ',
          'phir lauTā hai ḳhurshīd-e-jahāñ-tāb safar se \ phir nūr-e-sahar dast-o-garebāñ hai sahar se ',
          'ham par tumhārī chaah kā ilzām hī to hai \ dushnām to nahīñ hai ye ikrām hī to hai ',
          'dil o jaañ fidā-e-rāhe kabhī aa ke dekh hamdam \ sar-e-kū-e-dil-figārāñ shab-e-ārzū kā aalam ',
          'uTh kar to aa gae haiñ tirī bazm se magar \ kuchh dil hī jāntā hai ki kis dil se aae haiñ ',
          'tez hai aaj dard-e-dil saaqī \ talḳhi-e-mai ko tez-tar kar de ',
          'garmi-e-rashk se har anjuman-e-gul-badanāñ \ tazkira chheḌe tirī pairahan-ārāī kā ',
          'vo mire ho ke bhī mire na hue \ un ko apnā banā ke dekh liyā ',
          'aate aate mirā naam sā rah gayā \ us ke hoñToñ pe kuchh kāñptā rah gayā ',
          'jo tumhārī maan leñ nāsehā to rahegā dāman-e-dil meñ kyā \ na kisī adū kī adāvateñ na kisī sanam kī muravvateñ ',
          'dil-e-nādāñ tujhe huā kyā hai \ āḳhir is dard kī davā kyā hai ',
          "vahī chashma-e-baqā thā jise sab sarāb samjhe \ vahī ḳhvāb mo'tabar the jo ḳhayāl tak na pahuñche ",
          'rañg pairāhan kā ḳhushbū zulf lahrāne kā naam \ mausam-e-gul hai tumhāre baam par aane kā naam ',
          'the bazm meñ sab dūd-e-sar-e-bazm se shādāñ \ be-kār jalāyā hameñ raushan-nazrī ne ',
          'ashār mire yuuñ to zamāne ke liye haiñ \ kuchh sher faqat un ko sunāne ke liye haiñ ',
          'tirā lutf vajh-e-taskīñ na qarār sharh-e-ġham se \ ki haiñ dil meñ vo gile bhī jo malāl tak na pahuñche ',
          'garmī-e-shauq-e-nazārā kā asar to dekho \ gul khile jaate haiñ vo sāya-e-tar to dekho ',
          'umr guzregī imtihān meñ kyā \ daaġh hī deñge mujh ko daan meñ kyā ',
          'sar vahī hai to āstāñ hai vahī \ jaañ vahī hai to jān-e-jāñ hai vahī ',
          'mushkil haiñ agar hālāt vahāñ dil bech aaeñ jaañ de aaeñ \ dil vaalo kūcha-e-jānāñ meñ kyā aise bhī hālāt nahīñ ',
          'dilbarī Thahrā zabān-e-ḳhalq khulvāne kā naam \ ab nahīñ lete parī-rū zulf bikhrāne kā naam ',
          'apne chehre se jo zāhir hai chhupāeñ kaise \ terī marzī ke mutābiq nazar aaeñ kaise ',
          'ashk ḳhūnāb ho chale haiñ \ ġham kī rañgat badal chalī hai ',
          'kaf-e-bāġhbāñ pe bahār-e-gul kā hai qarz pahle se besh-tar \ ki har ek phuul ke pairahan meñ numūd mere lahū kī hai ',
          'rah-e-ḳhizāñ meñ talāsh-e-bahār karte rahe \ shab-e-siyah se talab husn-e-yār karte rahe ',
          'tirī diid se sivā hai tire shauq meñ bahārāñ \ vo chaman jahāñ girī hai tire gesuoñ kī shabnam ',
          'har koī shahr meñ phirtā hai salāmat-dāman \ riñd mai-ḳhāne se shāista-ḳhirām aatā hai ',
          'sahal yuuñ rāh-e-zindagī kī hai \ har qadam ham ne āshiqī kī hai ',
          'kis harf pe tū ne gosha-e-lab ai jān-e-jahāñ ġhammāz kiyā \ elān-e-junūñ dil vāloñ ne ab ke ba-hazār-andāz kiyā ',
          'dil rahīn-e-niyāz ho jaae \ bekasī kārsāz ho jaae ',
          'husn marhūn-e-josh-e-bāda-e-nāz \ ishq minnat-kash-e-fusūn-e-niyāz ',
          'ik gul ke murjhāne par kyā gulshan meñ kohrām machā \ ik chehra kumhlā jaane se kitne dil nāshād hue ',
          'gar intizār kaThin hai to jab talak ai dil \ kisī ke vāda-e-fardā kī guftugū hī sahī ',
          'jis dhaj se koī maqtal meñ gayā vo shaan salāmat rahtī hai \ ye jaan to aanī jaanī hai is jaañ kī to koī baat nahīñ ',
          'daulat-e-lab se phir ai ḳhusrav-e-shīrīñ-dahanāñ \ aaj arzāñ ho koī harf shanāsāī kā ',
          'kis tarah paak ho be-ārzū lamhoñ kā hisāb \ dard aayā nahīñ darbār sajāne kab se ',
          'tere dast-e-sitam kā ijz nahīñ \ dil hī kāfir thā jis ne aah na kī ',
          'qafas udaas hai yaaro sabā se kuchh to kaho \ kahīñ to bahr-e-ḳhudā aaj zikr-e-yār chale ',
          'kaise māneñ haram ke sahl-pasand \ rasm jo āshiqoñ ke diiñ kī hai ',
          'yak jaan na ho sakiye anjān na ban sakiye \ yuuñ TuuT gaī dil meñ shamshīr-e-shanāsāī ',
          'aao kareñ mahfil pe zar-e-zaḳhm numāyāñ \ charchā hai bahut be-sar-o-sāmānī-e-dil kā ',
          'sar karo saaz ki chheḌeñ koī dil-soz ġhazal \ DhūñDtā hai dil-e-shorīda bahāne kab se ',
          'fareb-e-ārzū kī sahl-añgārī nahīñ jaatī \ ham apne dil kī dhaḌkan ko tirī āvāz-e-pā samjhe ',
          'ummīd-e-talattuf meñ ranjīda rahe donoñ \ tū aur tirī mahfil maiñ aur mirī tanhāī ',
          'karo kaj jabīñ pe sar-e-kafan mire qātiloñ ko gumāñ na ho \ ki ġhurūr-e-ishq kā bāñkpan pas-e-marg ham ne bhulā diyā ',
          'kabhī kabhī aarzū ke sahrā meñ aa ke rukte haiñ qāfile se \ vo saarī bāteñ lagāv kī sī vo saare unvāñ visāl ke se ',
          'kiye aarzū se paimāñ jo maaal tak na pahuñche \ shab-o-roz-e-āshnāī mah o saal tak na pahuñche ',

          'sau paikāñ the paivast-e-gulū jab chheḌī shauq kī lai ham ne \ so tiir tarāzū the dil meñ jab ham ne raqs āġhāz kiyā ',
          'subh-e-gul ho ki shām-e-mai-ḳhāna \ madh us rū-e-nāznīñ kī hai ',
          'zahr se dho liye haiñ hoñT apne \ lutf-e-sāqī ne jab kamī kī hai ',
          'merī ḳhāmoshiyoñ meñ larzāñ hai \ mere nāloñ kī gum-shuda āvāz ',
          'na gañvāo nāvak-e-nīm-kash dil-e-reza-reza gañvā diyā \ jo bache haiñ sañg sameT lo tan-e-dāġh-dāġh luTā diyā ',
          'piyo ki muft lagā dī hai ḳhūn-e-dil kī kashīd \ girāñ hai ab ke mai-e-lāla-fām kahte haiñ ',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ',
          'mujh se pahlī sī mohabbat mirī mahbūb na maañg',
          'maiñ ne samjhā thā ki tū hai to daraḳhshāñ hai hayāt \ terā ġham hai to ġham-e-dahr kā jhagḌā kyā hai',
          'terī sūrat se hai aalam meñ bahāroñ ko sabāt \ terī āñkhoñ ke sivā duniyā meñ rakkhā kyā hai',
          'tū jo mil jaa.e to taqdīr nigūñ ho jaa.e \ yuuñ na thā maiñ ne faqat chāhā thā yuuñ ho jaa.e',
          'aur bhī dukh haiñ zamāne meñ mohabbat ke sivā \ rāhateñ aur bhī haiñ vasl kī rāhat ke sivā',
          'an-ginat sadiyoñ ke tārīk bahīmāna tilism \ resham o atlas o kamḳhāb meñ bunvā.e hue',
          'jā-ba-jā bikte hue kūcha-o-bāzār meñ jism \ ḳhaak meñ luThḌe hue ḳhuun meñ nahlā.e hue',
          'jism nikle hue amrāz ke tannūroñ se \ piip bahtī huī galte hue nāsūroñ se',
          'lauT jaatī hai udhar ko bhī nazar kyā kiije \ ab bhī dilkash hai tirā husn magar kyā kiije',
          'bol ki lab āzād haiñ tere \ bol zabāñ ab tak terī hai',
          'terā sutvāñ jism hai terā \ bol ki jaañ ab tak terī hai',
          'dekh ki āhan-gar kī dukāñ meñ \ tund haiñ sho.ale surḳh hai aahan',
          'khulne lage qufloñ ke dahāne \ phailā har ik zanjīr kā dāman',
          'bol ye thoḌā vaqt bahut hai \ jism o zabāñ kī maut se pahle',
          'bol ki sach zinda hai ab tak \ bol jo kuchh kahnā hai kah le',
          'chashm-nam jān-e-shorīda kaafī nahīñ \ tohmat-e-ishq-e-poshīda kaafī nahīñ',
          'aaj bāzār meñ pā-ba-jaulāñ chalo \ dast-afshāñ chalo mast o raqsāñ chalo',
          'ḳhāk-bar-sar chalo ḳhūñ-ba-dāmāñ chalo \ raah taktā hai sab shahr-e-jānāñ chalo',
          'hākim-e-shahr bhī majma-e-ām bhī \ tīr-e-ilzām bhī sañg-e-dushnām bhī',
          'sub.h-e-nāshād bhī roz-e-nākām bhī \ un kā dam-sāz apne sivā kaun hai',
          'shahr-e-jānāñ meñ ab bā-safā kaun hai \ dast-e-qātil ke shāyāñ rahā kaun hai',
          'raḳht-e-dil bāñdh lo dil-figāro chalo \ phir hamīñ qatl ho aa.eñ yaaro chalo',
          'aa ki vābasta haiñ us husn kī yādeñ tujh se \ jis ne is dil ko parī-ḳhāna banā rakkhā thā',
          'jis kī ulfat meñ bhulā rakkhī thī duniyā ham ne \ dahr ko dahr kā afsāna banā rakkhā thā',
          'āshnā haiñ tire qadmoñ se vo rāheñ jin par \ us kī mad.hosh javānī ne ināyat kī hai',
          'kārvāñ guzre haiñ jin se usī rānā.ī ke \ jis kī in āñkhoñ ne be-sūd ibādat kī hai',

          'tujh se khelī haiñ vo mahbūb havā.eñ jin meñ \ us ke malbūs kī afsurda mahak baaqī hai',

          'tujh pe barsā hai usī baam se mahtāb kā nuur \ jis meñ biitī huī rātoñ kī kasak baaqī hai',

          'tū ne dekhī hai vo peshānī vo ruḳhsār vo hoñT \ zindagī jin ke tasavvur meñ luTā dī ham ne',

          'tujh pe uTThī haiñ vo khoī huī sāhir āñkheñ \ tujh ko ma.alūm hai kyuuñ umr gañvā dī ham ne',

          'ham pe mushtarka haiñ ehsān ġham-e-ulfat ke \ itne ehsān ki ginvā.ūñ to ginvā na sakūñ',

          'ham ne is ishq meñ kyā khoyā hai kyā sīkhā hai \ juz tire aur ko samjhā.ūñ to samjhā na sakūñ',

          'ājizī sīkhī ġharīboñ kī himāyat sīkhī \ yās-o-hirmān ke dukh-dard ke ma.anī sīkhe',

          'zer-dastoñ ke masā.ib ko samajhnā sīkhā \ sard aahoñ ke ruḳh-e-zard ke ma.anī sīkhe',

          'jab kahīñ baiTh ke rote haiñ vo bekas jin ke \ ashk āñkhoñ meñ bilakte hue so jaate haiñ',

          'nā-tavānoñ ke nivāloñ pe jhapaTte haiñ uqaab \ baazū tole hue mañDlāte hue aate haiñ',

          'jab kabhī biktā hai bāzār meñ mazdūr kā gosht \ shāh-rāhoñ pe ġharīboñ kā lahū bahtā hai',

          "aag sī siine meñ rah rah ke ubaltī hai na pūchh \ apne dil par mujhe qaabū hī nahīñ rahtā hai",

          'ye galiyoñ ke āvāra be - kār kutte \ ki baḳhshā gayā jin ko zauq - e - gadā.ī',

          'zamāne kī phaTkār sarmāya in kā \ jahāñ bhar kī dhutkār in kī kamā.ī',

          'na ārām shab ko na rāhat savere \ ġhalāzat meñ ghar nāliyoñ meñ basere',

          'jo bigḌeñ to ik dūsre ko laḌā do \ zarā ek roTī kā TukḌā dikhā do',

          'ye har ek kī Thokareñ khāne vaale \ ye fāqoñ se uktā ke mar jaane vaale',

          'ye mazlūm maḳhlūq gar sar uThā.e \ to insān sab sar - kashī bhuul jaa.e',

          'ye chāheñ to duniyā ko apnā banā leñ \ ye āqāoñ kī haDDiyāñ tak chabā leñ',

          'koī in ko ehsās - e - zillat dilā de \ koī in kī soī huī dum hilā de',

          'gul huī jaatī hai afsurda sulagtī huī shaam \ Dhul ke niklegī abhī chashma-e-mahtāb se raat',

          'aur mushtāq nigāhoñ kī sunī jā.egī \ aur un hāthoñ se mas hoñge ye tarse hue haat',

          'un kā āñchal hai ki ruḳhsār ki pairāhan hai \ kuchh to hai jis se huī jaatī hai chilman rañgīñ',

          'jaane us zulf kī mauhūm ghanī chhāñv meñ \ TimTimātā hai vo āveza abhī tak ki nahīñ',

          'aaj phir husn-e-dil-ārā kī vahī dhaj hogī \ vahī ḳhvābīda sī āñkheñ vahī kājal kī lakīr',

          'rañg-e-rukHsār pe halkā sā vo ġhāze kā ġhubār \ sandalī haath pe dhuñdlī sī hinā kī tahrīr',

          'apne afkār kī ash.ār kī duniyā hai yahī \ jān-e-mazmūñ hai yahī shāhid-e-ma.anī hai yahī',

          'aaj tak surḳh o siyah sadiyoñ ke saa.e ke tale \ aadam o havvā kī aulād pe kyā guzrī hai?',

          'maut aur ziist kī rozāna saf-ārā.ī meñ \ ham pe kyā guzregī ajdād pe kyā guzrī hai?',

          'in damakte hue shahroñ kī farāvāñ maḳhlūq \ kyuuñ faqat marne kī hasrat meñ jiyā kartī hai',

          'ye hasīñ khet phaTā paḌtā hai jauban jin kaa! \ kis liye in meñ faqat bhuuk ugā kartī hai',

          'ye har ik samt pur-asrār kaḌī dīvāreñ \ jal-bujhe jin meñ hazāroñ kī javānī ke charāġh',

          'ye har ik gaam pe un ḳhvāboñ kī maqtal-gāheñ \ jin ke partav se charāġhāñ haiñ hazāroñ ke dimāġh',

          'ye bhī haiñ aise ka.ī aur bhī mazmūñ hoñge \ lekin us shoḳh ke āhista se khulte hue hoñT',

          'haa.e us jism ke kambaḳht dil-āvez ḳhutūt \ aap hī kahiye kahīñ aise bhī afsūñ hoñge',

          'apnā mauzu-e-suḳhan un ke sivā aur nahīñ \ tab.a-e-shā.er kā vatan un ke sivā aur nahīñ',

          'kar rahā thā ġham-e-jahāñ kā hisāb \ aaj tum yaad be-hisāb aa.e',

          'tumhārī yaad ke jab zaḳhm bharne lagte haiñ \ kisī bahāne tumheñ yaad karne lagte haiñ',
          'nahīñ nigāh meñ manzil to justujū hī sahī \ nahīñ visāl mayassar to aarzū hī sahī',
          'aa.e to yuuñ ki jaise hamesha the mehrbān \ bhūle to yuuñ ki goyā kabhī āshnā na the',
          'ye aarzū bhī baḌī chiiz hai magar hamdam \ visāl-e-yār faqat aarzū kī baat nahīñ',
          'ik fursat-e-gunāh milī vo bhī chaar din \ dekhe haiñ ham ne hausle parvardigār ke',
          'tere qaul-o-qarār se pahle \ apne kuchh aur bhī sahāre the']


# defining a function to read the most recent tweet_id

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


# defining a function to write the most recent tweet_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# defining the main reply function

last_tweet_id = str(1365434870772748290)


def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        random_verse = ' - ' + lyrics[randint(0, len(lyrics))]
        mention_plus_username = '@' + tweet.user.screen_name
        print(str(tweet.id), '-', tweet.full_text)
        api.update_status(mention_plus_username + random_verse, tweet.id)
        store_last_seen(FILE_NAME, tweet.id)


def reply():
    tweets = api.mentions_timeline(since_id=last_tweet_id, tweet_mode='extended')
    for tweet in reversed(tweets):
        random_verse = ' - ' + lyrics[randint(0, len(lyrics))]
        mention_plus_username = '@' + tweet.user.screen_name
        api.update_status(mention_plus_username + random_verse, tweet.id)
        last_tweet_id = str(tweet.id)



# defining the main tweet function

def send_tweet():
    api.update_status(" " + lyrics[randint(0, len(lyrics))])


# defining the main function by combining the two main functions

def main_code():
    send_tweet()
    time.sleep(60*60*4)
    #for i in range(480):
        #reply()
        #time.sleep(30)


while True:
    try:
        main_code()
    except tweepy.TweepError as e:
        # sometimes twitter is over capacity so sleep then continue
        if e.reason == "[{u'message': u'Over capacity', u'code': 130}]":
            time.sleep(30)
            continue
