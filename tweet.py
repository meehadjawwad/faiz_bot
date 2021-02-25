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

lyrics = ['sitam sikhlāegā rasm-e-vafā aise nahīñ hotā \ sanam dikhlāeñge rāh-e-ḳhudā aise nahīñ hotā ',
          'gino sab hasrateñ jo ḳhuuñ huī haiñ tan ke maqtal meñ \ mire qātil hisāb-e-ḳhūñ-bahā aise nahīñ hotā ',
          'jahān-e-dil meñ kaam aatī haiñ tadbīreñ na taazīreñ \ yahāñ paimān-e-taslīm-o-razā aise nahīñ hotā ',
          'har ik shab har ghaḌī guzre qayāmat yuuñ to hotā hai \ magar har subh ho roz-e-jazā aise nahīñ hotā ',
          'ravāñ hai nabz-e-daurāñ gardishoñ meñ āsmāñ saare \ jo tum kahte ho sab kuchh ho chukā aise nahīñ hotā ', '',
          '', '', '', '', 'ham saada hī aise the kī yuuñ hī pazīrāī \ jis baar ḳhizāñ aaī samjhe ki bahār aaī ', '',
          'husn marhūn-e-josh-e-bāda-e-nāz \ ishq minnat-kash-e-fusūn-e-niyāz ', '',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ', '',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ', '',
          'apne har har lafz kā ḳhud āīna ho jāūñgā \ us ko chhoTā kah ke maiñ kaise baḌā ho jāūñgā ', '',
          'aate aate mirā naam sā rah gayā \ us ke hoñToñ pe kuchh kāñptā rah gayā ', '',
          'apne chehre se jo zāhir hai chhupāeñ kaise \ terī marzī ke mutābiq nazar aaeñ kaise ', '',
          'yuuñ bahār aaī hai is baar ki jaise qāsid \ kūcha-e-yār se be-nail-e-marām aatā hai ',
          'har koī shahr meñ phirtā hai salāmat-dāman \ riñd mai-ḳhāne se shāista-ḳhirām aatā hai ',
          'havas-e-mutrib-o-sāqī meñ pareshāñ akasr \ abr aatā hai kabhī māh-e-tamām aatā hai ',
          'shauq vāloñ kī hazīñ mahfil-e-shab meñ ab bhī \ āmad-e-subh kī sūrat tirā naam aatā hai ',
          'ab bhī elān-e-sahar kartā huā mast koī \ dāġh-e-dil kar ke farozāñ sar-e-shām aatā hai ', '', '', '', '', '',
          'kis shahr na shohra huā nādānī-e-dil kā \ kis par na khulā raaz pareshānī-e-dil kā ', '',
          'phir lauTā hai ḳhurshīd-e-jahāñ-tāb safar se \ phir nūr-e-sahar dast-o-garebāñ hai sahar se ', '',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ', '',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ', '',
          'aap ko chehre se bhī bīmār honā chāhiye \ ishq hai to ishq kā izhār honā chāhiye ', '',
          'vahī phir mujhe yaad aane lage haiñ \ jinheñ bhūlne meñ zamāne lage haiñ ', '',
          'ik pal meñ ik sadī kā mazā ham se pūchhiye \ do din kī zindagī kā mazā ham se pūchhiye ', '',
          'kis harf pe tū ne gosha-e-lab ai jān-e-jahāñ ġhammāz kiyā \ elān-e-junūñ dil vāloñ ne ab ke ba-hazār-andāz kiyā ',
          'sau paikāñ the paivast-e-gulū jab chheḌī shauq kī lai ham ne \ so tiir tarāzū the dil meñ jab ham ne raqs āġhāz kiyā ',
          'be-hirs-o-havā be-ḳhauf-o-ḳhatar is haath pe sar is kaf pe jigar \ yuuñ kū-e-sanam meñ vaqt-e-safar nazzāra-e-bām-e-nāz kiyā ',
          'jis ḳhaak meñ mil kar ḳhaak hue vo surma-e-chashm-e-ḳhalq banī \ jis ḳhaar pe ham ne ḳhuuñ chhiḌkā ham-rañg-e-gul-e-tannāz kiyā ',
          'lo vasl kī saaat aa pahuñchī phir hukm-e-huzūrī par ham ne \ āñkhoñ ke darīche band kiye aur siine kā dar baaz kiyā ',
          '', '', '', '', '',
          'vo ahd-e-ġham kī kāhish-hā-e-be-hāsil ko kyā samjhe \ jo un kī muḳhtasar rūdād bhī sabr-āzmā samjhe ', '',
          'ijz-e-ahl-e-sitam kī baat karo \ ishq ke dam-qadam kī baat karo ', '',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ', '',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ', '',
          'umr guzregī imtihān meñ kyā \ daaġh hī deñge mujh ko daan meñ kyā ', '',
          'nayā ik rishta paidā kyuuñ kareñ ham \ bichhaḌnā hai to jhagḌā kyuuñ kareñ ham ', '',
          'be-qarārī sī be-qarārī hai \ vasl hai aur firāq taarī hai ', '',
          'jamegī kaise bisāt-e-yārāñ ki shīsha o jaam bujh gae haiñ \ sajegī kaise shab-e-nigārāñ ki dil sar-e-shām bujh gae haiñ ',
          'vo tīrgī hai rah-e-butāñ meñ charāġh-e-ruḳh hai na sham-e-vāda \ kiran koī aarzū kī laao ki sab dar-o-bām bujh gae haiñ ',
          'bahut sambhālā vafā kā paimāñ magar vo barsī hai ab ke barkhā \ har ek iqrār miT gayā hai tamām paiġhām bujh gae haiñ ',
          'qarīb aa ai mah-e-shab-e-ġham nazar pe khultā nahīñ kuchh is dam \ ki dil pe kis kis kā naqsh baaqī hai kaun se naam bujh gae haiñ ',
          'bahār ab aa ke kyā karegī ki jin se thā jashn-e-rañg-o-naġhma \ vo gul sar-e-shāḳh jal gae haiñ vo dil tah-e-dām bujh gae haiñ ',
          '', '', '', '', '',
          'yaad kā phir koī darvāza khulā āḳhir-e-shab \ dil meñ bikhrī koī ḳhushbu-e-qabā āḳhir-e-shab ', '',
          'rah-e-ḳhizāñ meñ talāsh-e-bahār karte rahe \ shab-e-siyah se talab husn-e-yār karte rahe ', '',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ', '',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ', '',
          'chupke chupke raat din aañsū bahānā yaad hai \ ham ko ab tak āshiqī kā vo zamānā yaad hai ', '',
          'aahaT sī koī aae to lagtā hai ki tum ho \ saaya koī lahrāe to lagtā hai ki tum ho ', '',
          'ashār mire yuuñ to zamāne ke liye haiñ \ kuchh sher faqat un ko sunāne ke liye haiñ ', '',
          'terī sūrat jo dil-nashīñ kī hai \ āshnā shakl har hasīñ kī hai ',
          'husn se dil lagā ke hastī kī \ har ghaḌī ham ne ātishīñ kī hai ',
          'subh-e-gul ho ki shām-e-mai-ḳhāna \ madh us rū-e-nāznīñ kī hai ',
          'shaiḳh se be-hirās milte haiñ \ ham ne tauba abhī nahīñ kī hai ',
          'zikr-e-dozaḳh bayān-e-hūr o qusūr \ baat goyā yahīñ kahīñ kī hai ',
          'ashk to kuchh bhī rañg lā na sake \ ḳhuuñ se tar aaj āstīñ kī hai ',
          'kaise māneñ haram ke sahl-pasand \ rasm jo āshiqoñ ke diiñ kī hai ',
          "'faiz' auj-e-ḳhayāl se ham ne \ āsmāñ sindh kī zamīñ kī hai ", '', '', '', '', '', '', '', '',
          'tujhe pukārā hai be-irāda \ jo dil dukhā hai bahut ziyāda ', '',
          'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī \ na karam hai ham pe habīb kā na nigāh ham pe ', '',
          'aae kuchh abr kuchh sharāb aae \ is ke baad aae jo azaab aae ', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ', '',
          'donoñ jahān terī mohabbat meñ haar ke \ vo jā rahā hai koī shab-e-ġham guzār ke ', '',
          'aah ko chāhiye ik umr asar hote tak \ kaun jiitā hai tirī zulf ke sar hote tak ', '',
          'dil-e-nādāñ tujhe huā kyā hai \ āḳhir is dard kī davā kyā hai ', '',
          'hazāroñ ḳhvāhisheñ aisī ki har ḳhvāhish pe dam nikle \ bahut nikle mire armān lekin phir bhī kam nikle ', '',
          'hasrat-e-dīd meñ guzarāñ haiñ zamāne kab se \ dasht-e-ummīd meñ gardāñ haiñ divāne kab se ',
          'der se aañkh pe utrā nahīñ ashkoñ kā azaab \ apne zimme hai tirā qarz na jaane kab se ',
          'kis tarah paak ho be-ārzū lamhoñ kā hisāb \ dard aayā nahīñ darbār sajāne kab se ',
          'sar karo saaz ki chheḌeñ koī dil-soz ġhazal \ DhūñDtā hai dil-e-shorīda bahāne kab se ',
          'pur karo jaam ki shāyad ho isī lahza ravāñ ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '',
          'tumhārī yaad ke jab zaḳhm bharne lagte haiñ \ kisī bahāne tumheñ yaad karne lagte haiñ ',
          'hadīs-e-yār ke unvāñ nikharne lagte haiñ \ to har harīm meñ gesū sañvarne lagte haiñ ',
          'har ajnabī hameñ mahram dikhāī detā hai \ jo ab bhī terī galī se guzarne lagte haiñ ',
          'sabā se karte haiñ ġhurbat-nasīb zikr-e-vatan \ to chashm-e-subh meñ aañsū ubharne lagte haiñ ',
          'vo jab bhī karte haiñ is nutq o lab kī baḳhiya-garī ', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '',
          'kiye aarzū se paimāñ jo maaal tak na pahuñche \ shab-o-roz-e-āshnāī mah o saal tak na pahuñche ',
          'vo nazar baham na pahuñchī ki muhīt-e-husn karte \ tirī diid ke vasīle ḳhad-o-ḳhāl tak na pahuñche ',
          "vahī chashma-e-baqā thā jise sab sarāb samjhe \ vahī ḳhvāb mo'tabar the jo ḳhayāl tak na pahuñche ",
          'tirā lutf vajh-e-taskīñ na qarār sharh-e-ġham se \ ki haiñ dil meñ vo gile bhī jo malāl tak na pahuñche ',
          'koī yaar jaañ se guzrā koī hosh se na guzrā ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '',
          'ham par tumhārī chaah kā ilzām hī to hai \ dushnām to nahīñ hai ye ikrām hī to hai ',
          'karte haiñ jis pe taan koī jurm to nahīñ \ shauq-e-fuzūl o ulfat-e-nākām hī to hai ',
          'dil muddaī ke harf-e-malāmat se shaad hai \ ai jān-e-jāñ ye harf tirā naam hī to hai ',
          'dil nā-umīd to nahīñ nākām hī to hai ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '',
          'sharh-e-firāq madh-e-lab-e-mushkbū kareñ \ ġhurbat-kade meñ kis se tirī guftugū kareñ ',
          'yaar āshnā nahīñ koī Takrāeñ kis se jaam \ kis dil-rubā ke naam pe ḳhālī subū kareñ ',
          'siine pe haath hai na nazar ko talāsh-e-bām \ dil saath de to aaj ġham-e-ārzū kareñ ',
          'kab tak sunegī raat kahāñ tak sunāeñ ham \ shikve-gile sab aaj tire rū-ba-rū kareñ ',
          'hamdam hadīs-e-kū-e-malāmat sunāiyo ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '',
          'kab yaad meñ terā saath nahīñ kab haat meñ terā haat nahīñ \ sad-shukr ki apnī rātoñ meñ ab hijr kī koī raat nahīñ ',
          'mushkil haiñ agar hālāt vahāñ dil bech aaeñ jaañ de aaeñ \ dil vaalo kūcha-e-jānāñ meñ kyā aise bhī hālāt nahīñ ',
          'jis dhaj se koī maqtal meñ gayā vo shaan salāmat rahtī hai \ ye jaan to aanī jaanī hai is jaañ kī to koī baat nahīñ ',
          'maidān-e-vafā darbār nahīñ yaañ nām-o-nasab kī pūchh kahāñ \ āshiq to kisī kā naam nahīñ kuchh ishq kisī kī zaat nahīñ ',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'husn marhūn-e-josh-e-bāda-e-nāz \ ishq minnat-kash-e-fusūn-e-niyāz ',
          'dil kā har taar larzish-e-paiham \ jaañ kā har rishta vaqf-e-soz-o-gudāz ',
          'sozish-e-dard-e-dil kise maalūm \ kaun jaane kisī ke ishq kā raaz ',
          'merī ḳhāmoshiyoñ meñ larzāñ hai \ mere nāloñ kī gum-shuda āvāz ', 'ho chukā ishq ab havas hī sahī ', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'vo ahd-e-ġham kī kāhish-hā-e-be-hāsil ko kyā samjhe \ jo un kī muḳhtasar rūdād bhī sabr-āzmā samjhe ',
          'yahāñ vābastagī vaañ barhamī kyā jāniye kyuuñ hai \ na ham apnī nazar samjhe na ham un kī adā samjhe ',
          'fareb-e-ārzū kī sahl-añgārī nahīñ jaatī \ ham apne dil kī dhaḌkan ko tirī āvāz-e-pā samjhe ',
          'tumhārī har nazar se munsalik hai rishta-e-hastī \ magar ye duur kī bāteñ koī nādān kyā samjhe ', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'na gañvāo nāvak-e-nīm-kash dil-e-reza-reza gañvā diyā \ jo bache haiñ sañg sameT lo tan-e-dāġh-dāġh luTā diyā ',
          'mire chāra-gar ko naved ho saf-e-dushmanāñ ko ḳhabar karo \ jo vo qarz rakhte the jaan par vo hisāb aaj chukā diyā ',
          'karo kaj jabīñ pe sar-e-kafan mire qātiloñ ko gumāñ na ho \ ki ġhurūr-e-ishq kā bāñkpan pas-e-marg ham ne bhulā diyā ',
          'udhar ek harf ki kushtanī yahāñ laakh uzr thā guftanī \ jo kahā to sun ke uḌā diyā jo likhā to paḌh ke miTā diyā ',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'vahīñ haiñ dil ke qarāin tamām kahte haiñ \ vo ik ḳhalish ki jise terā naam kahte haiñ ',
          'tum aa rahe ho ki bajtī haiñ merī zanjīreñ \ na jaane kyā mire dīvār-o-bām kahte haiñ ',
          'yahī kanār-e-falak kā siyah-tarīñ gosha \ yahī hai matla-e-māh-e-tamām kahte haiñ ',
          'piyo ki muft lagā dī hai ḳhūn-e-dil kī kashīd \ girāñ hai ab ke mai-e-lāla-fām kahte haiñ ',
          'faqīh-e-shahr se mai kā javāz kyā pūchheñ ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', 'sahal yuuñ rāh-e-zindagī kī hai \ har qadam ham ne āshiqī kī hai ',
          'ham ne dil meñ sajā liye gulshan \ jab bahāroñ ne be-ruḳhī kī hai ',
          'zahr se dho liye haiñ hoñT apne \ lutf-e-sāqī ne jab kamī kī hai ',
          'tere kūche meñ bādshāhī kī \ jab se nikle gadāgarī kī hai ', 'bas vahī surḳh-rū huā jis ne ', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'kabhī kabhī yaad meñ ubharte haiñ naqsh-e-māzī miTe miTe se \ vo āzmāish dil o nazar kī vo qurbateñ sī vo fāsle se ',
          'kabhī kabhī aarzū ke sahrā meñ aa ke rukte haiñ qāfile se \ vo saarī bāteñ lagāv kī sī vo saare unvāñ visāl ke se ',
          'nigāh o dil ko qarār kaisā nashāt o ġham meñ kamī kahāñ kī \ vo jab mile haiñ to un se har baar kī hai ulfat nae sire se ',
          'bahut girāñ hai ye aish-e-tanhā kahīñ subuk-tar kahīñ gavārā \ vo dard-e-pinhāñ ki saarī duniyā rafīq thī jis ke vāste se ',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'shaiḳh sāhab se rasm-o-rāh na kī \ shukr hai zindagī tabāh na kī ',
          'tujh ko dekhā to ser-chashm hue \ tujh ko chāhā to aur chaah na kī ',
          'tere dast-e-sitam kā ijz nahīñ \ dil hī kāfir thā jis ne aah na kī ',
          'the shab-e-hijr kaam aur bahut \ ham ne fikr-e-dil-e-tabāh na kī ', "kaun qātil bachā hai shahr meñ 'faiz' ",
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'har samt pareshāñ tirī aamad ke qarīne \ dhoke diye kyā kyā hameñ bād-e-saharī ne ',
          'har manzil-e-ġhurbat pe gumāñ hotā hai ghar kā \ bahlāyā hai har gaam bahut dar-ba-darī ne ',
          'the bazm meñ sab dūd-e-sar-e-bazm se shādāñ \ be-kār jalāyā hameñ raushan-nazrī ne ',
          'mai-ḳhāne meñ aajiz hue āzurda-dilī se \ masjid kā na rakkhā hameñ āshufta-sarī ne ',
          'ye jāma-e-sad-chāk badal lene meñ kyā thā ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '',
          'ye jafā-e-ġham kā chāra vo najāt-e-dil kā aalam \ tirā husn dast-e-īsā tirī yaad rū-e-maryam ',
          'dil o jaañ fidā-e-rāhe kabhī aa ke dekh hamdam \ sar-e-kū-e-dil-figārāñ shab-e-ārzū kā aalam ',
          'tirī diid se sivā hai tire shauq meñ bahārāñ \ vo chaman jahāñ girī hai tire gesuoñ kī shabnam ',
          'ye ajab qayāmateñ haiñ tire rahguzar meñ guzarāñ \ na huā ki mar miTeñ ham na huā ki jī uTheñ ham ',
          'lo sunī gaī hamārī yuuñ phire haiñ din ki phir se ', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', 'baat bas se nikal chalī hai \ dil kī hālat sambhal chalī hai ',
          'ab junūñ had se baḌh chalā hai \ ab tabīat bahal chalī hai ',
          'ashk ḳhūnāb ho chale haiñ \ ġham kī rañgat badal chalī hai ', 'yā yūñhī bujh rahī haiñ shameñ ', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'ab ke baras dastūr-e-sitam meñ kyā kyā baab īzād hue \ jo qātil the maqtūl hue jo said the ab sayyād hue ',
          'pahle bhī ḳhizāñ meñ baaġh ujḌe par yuuñ nahīñ jaise ab ke baras \ saare buuTe patta patta ravish ravish barbād hue ',
          "pahle bhī tavāf-e-sham-e-vafā thī rasm mohabbat vāloñ kī \ ham tum se pahle bhī yahāñ 'mansūr' hue 'farhād' hue ",
          'ik gul ke murjhāne par kyā gulshan meñ kohrām machā \ ik chehra kumhlā jaane se kitne dil nāshād hue ', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'chāñd nikle kisī jānib tirī zebāī kā \ rañg badle kisī sūrat shab-e-tanhāī kā ',
          'daulat-e-lab se phir ai ḳhusrav-e-shīrīñ-dahanāñ \ aaj arzāñ ho koī harf shanāsāī kā ',
          'garmi-e-rashk se har anjuman-e-gul-badanāñ \ tazkira chheḌe tirī pairahan-ārāī kā ',
          'sehn-e-gulshan meñ kabhī ai shah-e-shamshād-qadāñ \ phir nazar aae salīqa tirī raanāī kā ',
          'ek baar aur masīhā-e-dil-e-dil-zadagāñ ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', 'nahīñ nigāh meñ manzil to justujū hī sahī \ nahīñ visāl mayassar to aarzū hī sahī ',
          'na tan meñ ḳhuun farāham na ashk āñkhoñ meñ \ namāz-e-shauq to vājib hai be-vazū hī sahī ',
          'kisī tarah to jame bazm mai-kade vaalo \ nahīñ jo bāda-o-sāġhar to hāv-hū hī sahī ',
          'gar intizār kaThin hai to jab talak ai dil \ kisī ke vāda-e-fardā kī guftugū hī sahī ',
          'dayār-e-ġhair meñ mahram agar nahīñ koī ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '',
          'phir lauTā hai ḳhurshīd-e-jahāñ-tāb safar se \ phir nūr-e-sahar dast-o-garebāñ hai sahar se ',
          'phir aag bhaḌakne lagī har sāz-e-tarab meñ \ phir shoale lapakne lage har dīda-e-tar se ',
          'phir niklā hai dīvāna koī phūñk ke ghar ko \ kuchh kahtī hai har raah har ik rāhguzar se ',
          'vo rañg hai imsāl gulistāñ kī fazā kā \ ojhal huī dīvār-e-qafas hadd-e-nazar se ',
          'sāġhar to khanakte haiñ sharāb aae na aae ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', 'rāz-e-ulfat chhupā ke dekh liyā \ dil bahut kuchh jalā ke dekh liyā ',
          'aur kyā dekhne ko baaqī hai \ aap se dil lagā ke dekh liyā ',
          'vo mire ho ke bhī mire na hue \ un ko apnā banā ke dekh liyā ',
          'aaj un kī nazar meñ kuchh ham ne \ sab kī nazreñ bachā ke dekh liyā ',
          "'faiz' takmīl-e-ġham bhī ho na sakī ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', 'ham ne sab sher meñ sañvāre the \ ham se jitne suḳhan tumhāre the ',
          'rañg-o-ḳhushbū ke husn-o-ḳhūbī ke \ tum se the jitne istiāre the ',
          'tere qaul-o-qarār se pahle \ apne kuchh aur bhī sahāre the ', 'jab vo laal-o-gohar hisāb kiye ', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'ham saada hī aise the kī yuuñ hī pazīrāī \ jis baar ḳhizāñ aaī samjhe ki bahār aaī ',
          'āshob-e-nazar se kī ham ne chaman-ārāī \ jo shai bhī nazar aaī gul-rañg nazar aaī ',
          'ummīd-e-talattuf meñ ranjīda rahe donoñ \ tū aur tirī mahfil maiñ aur mirī tanhāī ',
          'yak jaan na ho sakiye anjān na ban sakiye \ yuuñ TuuT gaī dil meñ shamshīr-e-shanāsāī ',
          'us tan kī taraf dekho jo qatl-gah-e-dil hai ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '',
          'guloñ meñ rañg bhare bād-e-nau-bahār chale \ chale bhī aao ki gulshan kā kārobār chale ',
          'qafas udaas hai yaaro sabā se kuchh to kaho \ kahīñ to bahr-e-ḳhudā aaj zikr-e-yār chale ',
          'kabhī to subh tire kunj-e-lab se ho āġhāz \ kabhī to shab sar-e-kākul se mushk-bār chale ',
          'baḌā hai dard kā rishta ye dil ġharīb sahī ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '',
          'fikr-e-dildāri-e-gulzār karūñ yā na karūñ \ zikr-e-murġhān-e-giraftār karūñ yā na karūñ ',
          'qissa-e-sāzish-e-aġhyār kahūñ yā na kahūñ \ shikva-e-yār-e-tarah-dār karūñ yā na karūñ ',
          'jaane kyā vaza hai ab rasm-e-vafā kī ai dil \ vaz-e-derīna pe isrār karūñ yā na karūñ ',
          'jaane kis rañg meñ tafsīr kareñ ahl-e-havas ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '',
          'chashm-e-maigūñ zarā idhar kar de \ dast-e-qudrat ko be-asar kar de ',
          'tez hai aaj dard-e-dil saaqī \ talḳhi-e-mai ko tez-tar kar de ',
          'josh-e-vahshat hai tishna-kām abhī \ chāk-e-dāman ko tā jigar kar de ',
          'merī qismat se khelne vaale \ mujh ko qismat se be-ḳhabar kar de ', 'luT rahī hai mirī matā-e-niyāz ', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'rañg pairāhan kā ḳhushbū zulf lahrāne kā naam \ mausam-e-gul hai tumhāre baam par aane kā naam ',
          'dosto us chashm o lab kī kuchh kaho jis ke baġhair \ gulsitāñ kī baat rañgīñ hai na mai-ḳhāne kā naam ',
          'phir nazar meñ phuul mahke dil meñ phir shameñ jalīñ \ phir tasavvur ne liyā us bazm meñ jaane kā naam ',
          'dilbarī Thahrā zabān-e-ḳhalq khulvāne kā naam \ ab nahīñ lete parī-rū zulf bikhrāne kā naam ',
          'ab kisī lailā ko bhī iqrār-e-mahbūbī nahīñ ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '',
          'sab qatl ho ke tere muqābil se aae haiñ \ ham log surḳh-rū haiñ ki manzil se aae haiñ ',
          'sham-e-nazar ḳhayāl ke anjum jigar ke daaġh \ jitne charāġh haiñ tirī mahfil se aae haiñ ',
          'uTh kar to aa gae haiñ tirī bazm se magar \ kuchh dil hī jāntā hai ki kis dil se aae haiñ ',
          'har ik qadam ajal thā har ik gaam zindagī \ ham ghuum phir ke kūcha-e-qātil se aae haiñ ',
          "bād-e-ḳhizāñ kā shukr karo 'faiz' jis ke haath ", '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', 'phir harīf-e-bahār ho baiThe \ jaane kis kis ko aaj ro baiThe ',
          'thī magar itnī rāegāñ bhī na thī \ aaj kuchh zindagī se kho baiThe ',
          'tere dar tak pahuñch ke lauT aae \ ishq kī aabrū Dubo baiThe ',
          'saarī duniyā se duur ho jaae \ jo zarā tere paas ho baiThe ', 'na gaī terī be-ruḳhī na gaī ', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī hai \ na karam hai ham pe habīb kā na nigāh ham pe adū kī hai ',
          'saf-e-zāhidāñ hai to be-yaqīñ saf-e-mai-kashāñ hai to be-talab \ na vo subh vird-o-vazū kī hai na vo shaam jām-o-subū kī hai ',
          'na ye ġham nayā na sitam nayā ki tirī jafā kā gilā kareñ \ ye nazar thī pahle bhī muztarib ye kasak to dil meñ kabhū kī hai ',
          'kaf-e-bāġhbāñ pe bahār-e-gul kā hai qarz pahle se besh-tar \ ki har ek phuul ke pairahan meñ numūd mere lahū kī hai ',
          "nahīñ ḳhauf-e-roz-e-siyah hameñ ki hai 'faiz' zarf-e-nigāh meñ ", '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '',
          'shafaq kī raakh meñ jal bujh gayā sitāra-e-shām \ shab-e-firāq ke gesū fazā meñ lahrāe ',
          'koī pukāro ki ik umr hone aaī hai \ falak ko qāfila-e-roz-o-shām Thahrāe ',
          'ye zid hai yaad harīfān-e-bāda-paimā kī \ ki shab ko chāñd na nikle na din ko abr aae ',
          'sabā ne phir dar-e-zindāñ pe aa ke dī dastak \ sahar qarīb hai dil se kaho na ghabrāe ', '', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'garmī-e-shauq-e-nazārā kā asar to dekho \ gul khile jaate haiñ vo sāya-e-tar to dekho ',
          'aise nādāñ bhī na the jaañ se guzarne vaale \ nāseho pand-garo rāhguzar to dekho ',
          'vo to vo hai tumheñ ho jāegī ulfat mujh se \ ik nazar tum mire mahbūb-e-nazar to dekho ',
          'vo jo ab chaak garebāñ bhī nahīñ karte haiñ \ dekhne vaalo kabhī un kā jigar to dekho ',
          'dāman-e-dard ko gulzār banā rakkhā hai ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '',
          'jaise ham-bazm haiñ phir yār-e-tarah-dār se ham \ raat milte rahe apne dar-o-dīvār se ham ',
          'sarḳhushī meñ yūñhī dil-shād o ġhazal-ḳhvāñ guzre \ kū-e-qātil se kabhī kūcha-e-dildār se ham ',
          'kabhī manzil kabhī raste ne hameñ saath diyā \ har qadam uljhe rahe qāfila-sālār se ham ',
          'ham se be-bahra huī ab jaras-e-gul kī sadā \ varna vāqif the har ik rañg kī jhankār se ham ',
          "'faiz' jab chāhā jo kuchh chāhā sadā maañg liyā ", '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '',
          'sabhī kuchh hai terā diyā huā sabhī rāhateñ sabhī kulfateñ \ kabhī sohbateñ kabhī furqateñ kabhī dūriyāñ kabhī qurbateñ ',
          'ye suḳhan jo ham ne raqam kiye ye haiñ sab varaq tirī yaad ke \ koī lamha subh-e-visāl kā koī shām-e-hijr kī muddateñ ',
          'jo tumhārī maan leñ nāsehā to rahegā dāman-e-dil meñ kyā \ na kisī adū kī adāvateñ na kisī sanam kī muravvateñ ',
          'chalo aao tum ko dikhāeñ ham jo bachā hai maqtal-e-shahr meñ \ ye mazār ahl-e-safā ke haiñ ye haiñ ahl-e-sidq kī turbateñ ',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'shāḳh par ḳhūn-e-gul ravāñ hai vahī \ shoḳhī-e-rañg-e-gulsitāñ hai vahī ',
          'sar vahī hai to āstāñ hai vahī \ jaañ vahī hai to jān-e-jāñ hai vahī ',
          'ab jahāñ mehrbāñ nahīñ koī \ kūcha-e-yār mehrbāñ hai vahī ',
          'barq sau baar gir ke ḳhaak huī \ raunaq-e-ḳhāk-e-āshiyāñ hai vahī ', 'aaj kī shab visāl kī shab hai ', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          'kis shahr na shohra huā nādānī-e-dil kā \ kis par na khulā raaz pareshānī-e-dil kā ',
          'aao kareñ mahfil pe zar-e-zaḳhm numāyāñ \ charchā hai bahut be-sar-o-sāmānī-e-dil kā ',
          'dekh aaeñ chalo kū-e-nigārāñ kā ḳharāba \ shāyad koī mahram mile vīrānī-e-dil kā ',
          'pūchho to udhar tīr-fagan kaun hai yaaro \ sauñpā thā jise kaam nigahbānī-e-dil kā ',
          'dekho to kidhar aaj ruḳh-e-bād-e-sabā hai ', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
          '', '', '', '', '', '', '', 'har haqīqat majāz ho jaae \ kāfiroñ kī namāz ho jaae ',
          'dil rahīn-e-niyāz ho jaae \ bekasī kārsāz ho jaae ',
          'minnat-e-chāra-sāz kaun kare \ dard jab jāñ-navāz ho jaae ',
          'ishq dil meñ rahe to rusvā ho \ lab pe aae to raaz ho jaae ', 'lutf kā intizār kartā huuñ ', '', '', '', '',
          '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


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

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        random_verse = ' - ' + lyrics[randint(0, len(lyrics))]
        mention_plus_username = '@' + tweet.user.screen_name
        print(str(tweet.id), '-', tweet.full_text)
        api.update_status(mention_plus_username + random_verse, tweet.id)
        store_last_seen(FILE_NAME, tweet.id)


# defining the main tweet function

def send_tweet():
    api.update_status(" " + lyrics[randint(0, len(lyrics))])


# defining the main function by combining the two main functions

def main_code():
    send_tweet()
    for i in range(480):
        reply()
        time.sleep(30)


while True:
    try:
        main_code()
    except tweepy.TweepError as e:
        # sometimes twitter is over capacity so sleep then continue
        if e.reason == "[{u'message': u'Over capacity', u'code': 130}]":
            time.sleep(30)
            continue
