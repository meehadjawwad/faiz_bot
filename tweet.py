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

lyrics = ["'faiz' auj-e-ḳhayāl se ham ne \\ āsmāñ sindh kī zamīñ kī hai ",
 "'faiz' takmīl-e-ġham bhī ho na sakī ",
 'aa ki vābasta haiñ us husn kī yādeñ tujh se \\ jis ne is dil ko parī-ḳhāna banā rakkhā thā',
 'aa.e to yuuñ ki jaise hamesha the mehrbān \\ bhūle to yuuñ ki goyā kabhī āshnā na the',
 'aae kuchh abr kuchh sharāb aae \\ is ke baad aae jo azaab aae ',
 'aag sī siine meñ rah rah ke ubaltī hai na pūchh \\ apne dil par mujhe qaabū hī nahīñ rahtā hai',
 'aahaT sī koī aae to lagtā hai ki tum ho \\ saaya koī lahrāe to lagtā hai ki tum ho ',
 'aaj bāzār meñ pā-ba-jaulāñ chalo \\ dast-afshāñ chalo mast o raqsāñ chalo',
 'aaj phir husn-e-dil-ārā kī vahī dhaj hogī \\ vahī ḳhvābīda sī āñkheñ vahī kājal kī lakīr',
 'aaj tak surḳh o siyah sadiyoñ ke saa.e ke tale \\ aadam o havvā kī aulād pe kyā guzrī hai?',
 'aaj un kī nazar meñ kuchh ham ne \\ sab kī nazreñ bachā ke dekh liyā ',
 'aao kareñ mahfil pe zar-e-zaḳhm numāyāñ \\ charchā hai bahut be-sar-o-sāmānī-e-dil kā ',
 'aap ko chehre se bhī bīmār honā chāhiye \\ ishq hai to ishq kā izhār honā chāhiye ',
 'aate aate mirā naam sā rah gayā \\ us ke hoñToñ pe kuchh kāñptā rah gayā ',
 'ab bhī elān-e-sahar kartā huā mast koī \\ dāġh-e-dil kar ke farozāñ sar-e-shām aatā hai ',
 'ab jahāñ mehrbāñ nahīñ koī \\ kūcha-e-yār mehrbāñ hai vahī ',
 'ab junūñ had se baḌh chalā hai \\ ab tabīat bahal chalī hai ',
 'ab ke baras dastūr-e-sitam meñ kyā kyā baab īzād hue \\ jo qātil the maqtūl hue jo said the ab sayyād hue ',
 'aise nādāñ bhī na the jaañ se guzarne vaale \\ nāseho pand-garo rāhguzar to dekho ',
 'an-ginat sadiyoñ ke tārīk bahīmāna tilism \\ resham o atlas o kamḳhāb meñ bunvā.e hue',
 'apne afkār kī ash.ār kī duniyā hai yahī \\ jān-e-mazmūñ hai yahī shāhid-e-ma.anī hai yahī',
 'apnā mauzu-e-suḳhan un ke sivā aur nahīñ \\ tab.a-e-shā.er kā vatan un ke sivā aur nahīñ',
 'ashk to kuchh bhī rañg lā na sake \\ ḳhuuñ se tar aaj āstīñ kī hai ',
 'ashk ḳhūnāb ho chale haiñ \\ ġham kī rañgat badal chalī hai ',
 'aur bhī dukh haiñ zamāne meñ mohabbat ke sivā \\ rāhateñ aur bhī haiñ vasl kī rāhat ke sivā',
 'aur kyā dekhne ko baaqī hai \\ aap se dil lagā ke dekh liyā ',
 'aur mushtāq nigāhoñ kī sunī jā.egī \\ aur un hāthoñ se mas hoñge ye tarse hue haat',
 'baat bas se nikal chalī hai \\ dil kī hālat sambhal chalī hai ',
 'bahut girāñ hai ye aish-e-tanhā kahīñ subuk-tar kahīñ gavārā \\ vo dard-e-pinhāñ ki saarī duniyā rafīq thī jis ke vāste se ',
 'bahut sambhālā vafā kā paimāñ magar vo barsī hai ab ke barkhā \\ har ek iqrār miT gayā hai tamām paiġhām bujh gae haiñ ',
 'bahār ab aa ke kyā karegī ki jin se thā jashn-e-rañg-o-naġhma \\ vo gul sar-e-shāḳh jal gae haiñ vo dil tah-e-dām bujh gae haiñ ',
 'barq sau baar gir ke ḳhaak huī \\ raunaq-e-ḳhāk-e-āshiyāñ hai vahī ',
 'be-hirs-o-havā be-ḳhauf-o-ḳhatar is haath pe sar is kaf pe jigar \\ yuuñ kū-e-sanam meñ vaqt-e-safar nazzāra-e-bām-e-nāz kiyā ',
 'be-qarārī sī be-qarārī hai \\ vasl hai aur firāq taarī hai ',
 'bol ki lab āzād haiñ tere \\ bol zabāñ ab tak terī hai',
 'bol ki sach zinda hai ab tak \\ bol jo kuchh kahnā hai kah le',
 'bol ye thoḌā vaqt bahut hai \\ jism o zabāñ kī maut se pahle',
 'chalo aao tum ko dikhāeñ ham jo bachā hai maqtal-e-shahr meñ \\ ye mazār ahl-e-safā ke haiñ ye haiñ ahl-e-sidq kī turbateñ ',
 'chashm-e-maigūñ zarā idhar kar de \\ dast-e-qudrat ko be-asar kar de ',
 'chashm-nam jān-e-shorīda kaafī nahīñ \\ tohmat-e-ishq-e-poshīda kaafī nahīñ',
 'chāñd nikle kisī jānib tirī zebāī kā \\ rañg badle kisī sūrat shab-e-tanhāī kā ',
 'daulat-e-lab se phir ai ḳhusrav-e-shīrīñ-dahanāñ \\ aaj arzāñ ho koī harf shanāsāī kā ',
 'dekh aaeñ chalo kū-e-nigārāñ kā ḳharāba \\ shāyad koī mahram mile vīrānī-e-dil kā ',
 'dekh ki āhan-gar kī dukāñ meñ \\ tund haiñ sho.ale surḳh hai aahan',
 'der se aañkh pe utrā nahīñ ashkoñ kā azaab \\ apne zimme hai tirā qarz na jaane kab se ',
 'dil kā har taar larzish-e-paiham \\ jaañ kā har rishta vaqf-e-soz-o-gudāz ',
 'dil muddaī ke harf-e-malāmat se shaad hai \\ ai jān-e-jāñ ye harf tirā naam hī to hai ',
 'dil nā-umīd to nahīñ nākām hī to hai ',
 'dil o jaañ fidā-e-rāhe kabhī aa ke dekh hamdam \\ sar-e-kū-e-dil-figārāñ shab-e-ārzū kā aalam ',
 'dil rahīn-e-niyāz ho jaae \\ bekasī kārsāz ho jaae ',
 'dilbarī Thahrā zabān-e-ḳhalq khulvāne kā naam \\ ab nahīñ lete parī-rū zulf bikhrāne kā naam ',
 'donoñ jahān terī mohabbat meñ haar ke \\ vo jā rahā hai koī shab-e-ġham guzār ke ',
 'dosto us chashm o lab kī kuchh kaho jis ke baġhair \\ gulsitāñ kī baat rañgīñ hai na mai-ḳhāne kā naam ',
 'dāman-e-dard ko gulzār banā rakkhā hai ',
 'fareb-e-ārzū kī sahl-añgārī nahīñ jaatī \\ ham apne dil kī dhaḌkan ko tirī āvāz-e-pā samjhe ',
 'fikr-e-dildāri-e-gulzār karūñ yā na karūñ \\ zikr-e-murġhān-e-giraftār karūñ yā na karūñ ',
 'gar intizār kaThin hai to jab talak ai dil \\ kisī ke vāda-e-fardā kī guftugū hī sahī ',
 'garmi-e-rashk se har anjuman-e-gul-badanāñ \\ tazkira chheḌe tirī pairahan-ārāī kā ',
 'garmī-e-shauq-e-nazārā kā asar to dekho \\ gul khile jaate haiñ vo sāya-e-tar to dekho ',
 'gino sab hasrateñ jo ḳhuuñ huī haiñ tan ke maqtal meñ \\ mire qātil hisāb-e-ḳhūñ-bahā aise nahīñ hotā ',
 'gul huī jaatī hai afsurda sulagtī huī shaam \\ Dhul ke niklegī abhī chashma-e-mahtāb se raat',
 'guloñ meñ rañg bhare bād-e-nau-bahār chale \\ chale bhī aao ki gulshan kā kārobār chale ',
 'haa.e us jism ke kambaḳht dil-āvez ḳhutūt \\ aap hī kahiye kahīñ aise bhī afsūñ hoñge',
 'hadīs-e-yār ke unvāñ nikharne lagte haiñ \\ to har harīm meñ gesū sañvarne lagte haiñ ',
 'ham ne dil meñ sajā liye gulshan \\ jab bahāroñ ne be-ruḳhī kī hai ',
 'ham ne is ishq meñ kyā khoyā hai kyā sīkhā hai \\ juz tire aur ko samjhā.ūñ to samjhā na sakūñ',
 'ham ne sab sher meñ sañvāre the \\ ham se jitne suḳhan tumhāre the ',
 'ham par tumhārī chaah kā ilzām hī to hai \\ dushnām to nahīñ hai ye ikrām hī to hai ',
 'ham pe mushtarka haiñ ehsān ġham-e-ulfat ke \\ itne ehsān ki ginvā.ūñ to ginvā na sakūñ',
 'ham saada hī aise the kī yuuñ hī pazīrāī \\ jis baar ḳhizāñ aaī samjhe ki bahār aaī ',
 'ham se be-bahra huī ab jaras-e-gul kī sadā \\ varna vāqif the har ik rañg kī jhankār se ham ',
 'har ajnabī hameñ mahram dikhāī detā hai \\ jo ab bhī terī galī se guzarne lagte haiñ ',
 'har haqīqat majāz ho jaae \\ kāfiroñ kī namāz ho jaae ',
 'har ik qadam ajal thā har ik gaam zindagī \\ ham ghuum phir ke kūcha-e-qātil se aae haiñ ',
 'har ik shab har ghaḌī guzre qayāmat yuuñ to hotā hai \\ magar har subh ho roz-e-jazā aise nahīñ hotā ',
 'har koī shahr meñ phirtā hai salāmat-dāman \\ riñd mai-ḳhāne se shāista-ḳhirām aatā hai ',
 'har manzil-e-ġhurbat pe gumāñ hotā hai ghar kā \\ bahlāyā hai har gaam bahut dar-ba-darī ne ',
 'har samt pareshāñ tirī aamad ke qarīne \\ dhoke diye kyā kyā hameñ bād-e-saharī ne ',
 'hasrat-e-dīd meñ guzarāñ haiñ zamāne kab se \\ dasht-e-ummīd meñ gardāñ haiñ divāne kab se ',
 'havas-e-mutrib-o-sāqī meñ pareshāñ akasr \\ abr aatā hai kabhī māh-e-tamām aatā hai ',
 'husn marhūn-e-josh-e-bāda-e-nāz \\ ishq minnat-kash-e-fusūn-e-niyāz ',
 'husn se dil lagā ke hastī kī \\ har ghaḌī ham ne ātishīñ kī hai ',
 'hākim-e-shahr bhī majma-e-ām bhī \\ tīr-e-ilzām bhī sañg-e-dushnām bhī',
 'ijz-e-ahl-e-sitam kī baat karo \\ ishq ke dam-qadam kī baat karo ',
 'ik fursat-e-gunāh milī vo bhī chaar din \\ dekhe haiñ ham ne hausle parvardigār ke',
 'ik gul ke murjhāne par kyā gulshan meñ kohrām machā \\ ik chehra kumhlā jaane se kitne dil nāshād hue ',
 'ik pal meñ ik sadī kā mazā ham se pūchhiye \\ do din kī zindagī kā mazā ham se pūchhiye ',
 'in damakte hue shahroñ kī farāvāñ maḳhlūq \\ kyuuñ faqat marne kī hasrat meñ jiyā kartī hai',
 'ishq dil meñ rahe to rusvā ho \\ lab pe aae to raaz ho jaae ',
 'jaane kyā vaza hai ab rasm-e-vafā kī ai dil \\ vaz-e-derīna pe isrār karūñ yā na karūñ ',
 'jaane us zulf kī mauhūm ghanī chhāñv meñ \\ TimTimātā hai vo āveza abhī tak ki nahīñ',
 'jab kabhī biktā hai bāzār meñ mazdūr kā gosht \\ shāh-rāhoñ pe ġharīboñ kā lahū bahtā hai',
 'jab kahīñ baiTh ke rote haiñ vo bekas jin ke \\ ashk āñkhoñ meñ bilakte hue so jaate haiñ',
 'jahān-e-dil meñ kaam aatī haiñ tadbīreñ na taazīreñ \\ yahāñ paimān-e-taslīm-o-razā aise nahīñ hotā ',
 'jaise ham-bazm haiñ phir yār-e-tarah-dār se ham \\ raat milte rahe apne dar-o-dīvār se ham ',
 'jamegī kaise bisāt-e-yārāñ ki shīsha o jaam bujh gae haiñ \\ sajegī kaise shab-e-nigārāñ ki dil sar-e-shām bujh gae haiñ ',
 'jis dhaj se koī maqtal meñ gayā vo shaan salāmat rahtī hai \\ ye jaan to aanī jaanī hai is jaañ kī to koī baat nahīñ ',
 'jis kī ulfat meñ bhulā rakkhī thī duniyā ham ne \\ dahr ko dahr kā afsāna banā rakkhā thā',
 'jis ḳhaak meñ mil kar ḳhaak hue vo surma-e-chashm-e-ḳhalq banī \\ jis ḳhaar pe ham ne ḳhuuñ chhiḌkā ham-rañg-e-gul-e-tannāz kiyā ',
 'jism nikle hue amrāz ke tannūroñ se \\ piip bahtī huī galte hue nāsūroñ se',
 'jo bigḌeñ to ik dūsre ko laḌā do \\ zarā ek roTī kā TukḌā dikhā do',
 'jo tumhārī maan leñ nāsehā to rahegā dāman-e-dil meñ kyā \\ na kisī adū kī adāvateñ na kisī sanam kī muravvateñ ',
 'josh-e-vahshat hai tishna-kām abhī \\ chāk-e-dāman ko tā jigar kar de ',
 'jā-ba-jā bikte hue kūcha-o-bāzār meñ jism \\ ḳhaak meñ luThḌe hue ḳhuun meñ nahlā.e hue',
 'kab tak sunegī raat kahāñ tak sunāeñ ham \\ shikve-gile sab aaj tire rū-ba-rū kareñ ',
 'kab yaad meñ terā saath nahīñ kab haat meñ terā haat nahīñ \\ sad-shukr ki apnī rātoñ meñ ab hijr kī koī raat nahīñ ',
 'kabhī kabhī aarzū ke sahrā meñ aa ke rukte haiñ qāfile se \\ vo saarī bāteñ lagāv kī sī vo saare unvāñ visāl ke se ',
 'kabhī kabhī yaad meñ ubharte haiñ naqsh-e-māzī miTe miTe se \\ vo āzmāish dil o nazar kī vo qurbateñ sī vo fāsle se ',
 'kabhī manzil kabhī raste ne hameñ saath diyā \\ har qadam uljhe rahe qāfila-sālār se ham ',
 'kabhī to subh tire kunj-e-lab se ho āġhāz \\ kabhī to shab sar-e-kākul se mushk-bār chale ',
 'kaf-e-bāġhbāñ pe bahār-e-gul kā hai qarz pahle se besh-tar \\ ki har ek phuul ke pairahan meñ numūd mere lahū kī hai ',
 'kaise māneñ haram ke sahl-pasand \\ rasm jo āshiqoñ ke diiñ kī hai ',
 'kar rahā thā ġham-e-jahāñ kā hisāb \\ aaj tum yaad be-hisāb aa.e',
 'karo kaj jabīñ pe sar-e-kafan mire qātiloñ ko gumāñ na ho \\ ki ġhurūr-e-ishq kā bāñkpan pas-e-marg ham ne bhulā diyā ',
 'karte haiñ jis pe taan koī jurm to nahīñ \\ shauq-e-fuzūl o ulfat-e-nākām hī to hai ',
 "kaun qātil bachā hai shahr meñ 'faiz' ",
 'khulne lage qufloñ ke dahāne \\ phailā har ik zanjīr kā dāman',
 'kis harf pe tū ne gosha-e-lab ai jān-e-jahāñ ġhammāz kiyā \\ elān-e-junūñ dil vāloñ ne ab ke ba-hazār-andāz kiyā ',
 'kis shahr na shohra huā nādānī-e-dil kā \\ kis par na khulā raaz pareshānī-e-dil kā ',
 'kis tarah paak ho be-ārzū lamhoñ kā hisāb \\ dard aayā nahīñ darbār sajāne kab se ',
 'kisī tarah to jame bazm mai-kade vaalo \\ nahīñ jo bāda-o-sāġhar to hāv-hū hī sahī ',
 'kiye aarzū se paimāñ jo maaal tak na pahuñche \\ shab-o-roz-e-āshnāī mah o saal tak na pahuñche ',
 'koī in ko ehsās - e - zillat dilā de \\ koī in kī soī huī dum hilā de',
 'koī pukāro ki ik umr hone aaī hai \\ falak ko qāfila-e-roz-o-shām Thahrāe ',
 'kārvāñ guzre haiñ jin se usī rānā.ī ke \\ jis kī in āñkhoñ ne be-sūd ibādat kī hai',
 'lauT jaatī hai udhar ko bhī nazar kyā kiije \\ ab bhī dilkash hai tirā husn magar kyā kiije',
 'lo sunī gaī hamārī yuuñ phire haiñ din ki phir se ',
 'lo vasl kī saaat aa pahuñchī phir hukm-e-huzūrī par ham ne \\ āñkhoñ ke darīche band kiye aur siine kā dar baaz kiyā ',
 'mai-ḳhāne meñ aajiz hue āzurda-dilī se \\ masjid kā na rakkhā hameñ āshufta-sarī ne ',
 'maidān-e-vafā darbār nahīñ yaañ nām-o-nasab kī pūchh kahāñ \\ āshiq to kisī kā naam nahīñ kuchh ishq kisī kī zaat nahīñ ',
 'maiñ ne samjhā thā ki tū hai to daraḳhshāñ hai hayāt \\ terā ġham hai to ġham-e-dahr kā jhagḌā kyā hai',
 'maut aur ziist kī rozāna saf-ārā.ī meñ \\ ham pe kyā guzregī ajdād pe kyā guzrī hai?',
 'merī qismat se khelne vaale \\ mujh ko qismat se be-ḳhabar kar de ',
 'merī ḳhāmoshiyoñ meñ larzāñ hai \\ mere nāloñ kī gum-shuda āvāz ',
 'minnat-e-chāra-sāz kaun kare \\ dard jab jāñ-navāz ho jaae ',
 'mire chāra-gar ko naved ho saf-e-dushmanāñ ko ḳhabar karo \\ jo vo qarz rakhte the jaan par vo hisāb aaj chukā diyā ',
 'mujh se pahlī sī mohabbat mirī mahbūb na maañg',
 'mushkil haiñ agar hālāt vahāñ dil bech aaeñ jaañ de aaeñ \\ dil vaalo kūcha-e-jānāñ meñ kyā aise bhī hālāt nahīñ ',
 'na gañvāo nāvak-e-nīm-kash dil-e-reza-reza gañvā diyā \\ jo bache haiñ sañg sameT lo tan-e-dāġh-dāġh luTā diyā ',
 'na gaī terī be-ruḳhī na gaī ',
 'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī \\ na karam hai ham pe habīb kā na nigāh ham pe ',
 'na kisī pe zaḳhm ayaañ koī na kisī ko fikr rafū kī hai \\ na karam hai ham pe habīb kā na nigāh ham pe adū kī hai ',
 'na tan meñ ḳhuun farāham na ashk āñkhoñ meñ \\ namāz-e-shauq to vājib hai be-vazū hī sahī ',
 'na ye ġham nayā na sitam nayā ki tirī jafā kā gilā kareñ \\ ye nazar thī pahle bhī muztarib ye kasak to dil meñ kabhū kī hai ',
 'na ārām shab ko na rāhat savere \\ ġhalāzat meñ ghar nāliyoñ meñ basere',
 'nahīñ nigāh meñ manzil to justujū hī sahī \\ nahīñ visāl mayassar to aarzū hī sahī',
 'nahīñ nigāh meñ manzil to justujū hī sahī \\ nahīñ visāl mayassar to aarzū hī sahī ',
 "nahīñ ḳhauf-e-roz-e-siyah hameñ ki hai 'faiz' zarf-e-nigāh meñ ",
 'nayā ik rishta paidā kyuuñ kareñ ham \\ bichhaḌnā hai to jhagḌā kyuuñ kareñ ham ',
 'nigāh o dil ko qarār kaisā nashāt o ġham meñ kamī kahāñ kī \\ vo jab mile haiñ to un se har baar kī hai ulfat nae sire se ',
 'nā-tavānoñ ke nivāloñ pe jhapaTte haiñ uqaab \\ baazū tole hue mañDlāte hue aate haiñ',
 "pahle bhī tavāf-e-sham-e-vafā thī rasm mohabbat vāloñ kī \\ ham tum se pahle bhī yahāñ 'mansūr' hue 'farhād' hue ",
 'pahle bhī ḳhizāñ meñ baaġh ujḌe par yuuñ nahīñ jaise ab ke baras \\ saare buuTe patta patta ravish ravish barbād hue ',
 'phir aag bhaḌakne lagī har sāz-e-tarab meñ \\ phir shoale lapakne lage har dīda-e-tar se ',
 'phir harīf-e-bahār ho baiThe \\ jaane kis kis ko aaj ro baiThe ',
 'phir lauTā hai ḳhurshīd-e-jahāñ-tāb safar se \\ phir nūr-e-sahar dast-o-garebāñ hai sahar se ',
 'phir nazar meñ phuul mahke dil meñ phir shameñ jalīñ \\ phir tasavvur ne liyā us bazm meñ jaane kā naam ',
 'phir niklā hai dīvāna koī phūñk ke ghar ko \\ kuchh kahtī hai har raah har ik rāhguzar se ',
 'piyo ki muft lagā dī hai ḳhūn-e-dil kī kashīd \\ girāñ hai ab ke mai-e-lāla-fām kahte haiñ ',
 'pūchho to udhar tīr-fagan kaun hai yaaro \\ sauñpā thā jise kaam nigahbānī-e-dil kā ',
 'qafas udaas hai yaaro sabā se kuchh to kaho \\ kahīñ to bahr-e-ḳhudā aaj zikr-e-yār chale ',
 'qarīb aa ai mah-e-shab-e-ġham nazar pe khultā nahīñ kuchh is dam \\ ki dil pe kis kis kā naqsh baaqī hai kaun se naam bujh gae haiñ ',
 'qissa-e-sāzish-e-aġhyār kahūñ yā na kahūñ \\ shikva-e-yār-e-tarah-dār karūñ yā na karūñ ',
 'rah-e-ḳhizāñ meñ talāsh-e-bahār karte rahe \\ shab-e-siyah se talab husn-e-yār karte rahe ',
 'ravāñ hai nabz-e-daurāñ gardishoñ meñ āsmāñ saare \\ jo tum kahte ho sab kuchh ho chukā aise nahīñ hotā ',
 'rañg pairāhan kā ḳhushbū zulf lahrāne kā naam \\ mausam-e-gul hai tumhāre baam par aane kā naam ',
 'rañg-e-rukHsār pe halkā sā vo ġhāze kā ġhubār \\ sandalī haath pe dhuñdlī sī hinā kī tahrīr',
 'rañg-o-ḳhushbū ke husn-o-ḳhūbī ke \\ tum se the jitne istiāre the ',
 'raḳht-e-dil bāñdh lo dil-figāro chalo \\ phir hamīñ qatl ho aa.eñ yaaro chalo',
 'rāz-e-ulfat chhupā ke dekh liyā \\ dil bahut kuchh jalā ke dekh liyā ',
 'saarī duniyā se duur ho jaae \\ jo zarā tere paas ho baiThe ',
 'sab qatl ho ke tere muqābil se aae haiñ \\ ham log surḳh-rū haiñ ki manzil se aae haiñ ',
 'sabhī kuchh hai terā diyā huā sabhī rāhateñ sabhī kulfateñ \\ kabhī sohbateñ kabhī furqateñ kabhī dūriyāñ kabhī qurbateñ ',
 'sabā ne phir dar-e-zindāñ pe aa ke dī dastak \\ sahar qarīb hai dil se kaho na ghabrāe ',
 'sabā se karte haiñ ġhurbat-nasīb zikr-e-vatan \\ to chashm-e-subh meñ aañsū ubharne lagte haiñ ',
 'saf-e-zāhidāñ hai to be-yaqīñ saf-e-mai-kashāñ hai to be-talab \\ na vo subh vird-o-vazū kī hai na vo shaam jām-o-subū kī hai ',
 'sahal yuuñ rāh-e-zindagī kī hai \\ har qadam ham ne āshiqī kī hai ',
 'sar karo saaz ki chheḌeñ koī dil-soz ġhazal \\ DhūñDtā hai dil-e-shorīda bahāne kab se ',
 'sar vahī hai to āstāñ hai vahī \\ jaañ vahī hai to jān-e-jāñ hai vahī ',
 'sarḳhushī meñ yūñhī dil-shād o ġhazal-ḳhvāñ guzre \\ kū-e-qātil se kabhī kūcha-e-dildār se ham ',
 'sau paikāñ the paivast-e-gulū jab chheḌī shauq kī lai ham ne \\ so tiir tarāzū the dil meñ jab ham ne raqs āġhāz kiyā ',
 'sehn-e-gulshan meñ kabhī ai shah-e-shamshād-qadāñ \\ phir nazar aae salīqa tirī raanāī kā ',
 'shafaq kī raakh meñ jal bujh gayā sitāra-e-shām \\ shab-e-firāq ke gesū fazā meñ lahrāe ',
 'shahr-e-jānāñ meñ ab bā-safā kaun hai \\ dast-e-qātil ke shāyāñ rahā kaun hai',
 'shaiḳh se be-hirās milte haiñ \\ ham ne tauba abhī nahīñ kī hai ',
 'shaiḳh sāhab se rasm-o-rāh na kī \\ shukr hai zindagī tabāh na kī ',
 'sham-e-nazar ḳhayāl ke anjum jigar ke daaġh \\ jitne charāġh haiñ tirī mahfil se aae haiñ ',
 'sharh-e-firāq madh-e-lab-e-mushkbū kareñ \\ ġhurbat-kade meñ kis se tirī guftugū kareñ ',
 'shauq vāloñ kī hazīñ mahfil-e-shab meñ ab bhī \\ āmad-e-subh kī sūrat tirā naam aatā hai ',
 'shāḳh par ḳhūn-e-gul ravāñ hai vahī \\ shoḳhī-e-rañg-e-gulsitāñ hai vahī ',
 'siine pe haath hai na nazar ko talāsh-e-bām \\ dil saath de to aaj ġham-e-ārzū kareñ ',
 'sitam sikhlāegā rasm-e-vafā aise nahīñ hotā \\ sanam dikhlāeñge rāh-e-ḳhudā aise nahīñ hotā ',
 'sozish-e-dard-e-dil kise maalūm \\ kaun jaane kisī ke ishq kā raaz ',
 'sub.h-e-nāshād bhī roz-e-nākām bhī \\ un kā dam-sāz apne sivā kaun hai',
 'subh-e-gul ho ki shām-e-mai-ḳhāna \\ madh us rū-e-nāznīñ kī hai ',
 'tere dar tak pahuñch ke lauT aae \\ ishq kī aabrū Dubo baiThe ',
 'tere dast-e-sitam kā ijz nahīñ \\ dil hī kāfir thā jis ne aah na kī ',
 'tere kūche meñ bādshāhī kī \\ jab se nikle gadāgarī kī hai ',
 'tere qaul-o-qarār se pahle \\ apne kuchh aur bhī sahāre the',
 'terā sutvāñ jism hai terā \\ bol ki jaañ ab tak terī hai',
 'terī sūrat jo dil-nashīñ kī hai \\ āshnā shakl har hasīñ kī hai ',
 'terī sūrat se hai aalam meñ bahāroñ ko sabāt \\ terī āñkhoñ ke sivā duniyā meñ rakkhā kyā hai',
 'tez hai aaj dard-e-dil saaqī \\ talḳhi-e-mai ko tez-tar kar de ',
 'the bazm meñ sab dūd-e-sar-e-bazm se shādāñ \\ be-kār jalāyā hameñ raushan-nazrī ne ',
 'the shab-e-hijr kaam aur bahut \\ ham ne fikr-e-dil-e-tabāh na kī ',
 'thī magar itnī rāegāñ bhī na thī \\ aaj kuchh zindagī se kho baiThe ',
 'tirā lutf vajh-e-taskīñ na qarār sharh-e-ġham se \\ ki haiñ dil meñ vo gile bhī jo malāl tak na pahuñche ',
 'tirī diid se sivā hai tire shauq meñ bahārāñ \\ vo chaman jahāñ girī hai tire gesuoñ kī shabnam ',
 'tujh ko dekhā to ser-chashm hue \\ tujh ko chāhā to aur chaah na kī ',
 'tujh pe barsā hai usī baam se mahtāb kā nuur \\ jis meñ biitī huī rātoñ kī kasak baaqī hai',
 'tujh pe uTThī haiñ vo khoī huī sāhir āñkheñ \\ tujh ko ma.alūm hai kyuuñ umr gañvā dī ham ne',
 'tujh se khelī haiñ vo mahbūb havā.eñ jin meñ \\ us ke malbūs kī afsurda mahak baaqī hai',
 'tujhe pukārā hai be-irāda \\ jo dil dukhā hai bahut ziyāda ',
 'tum aa rahe ho ki bajtī haiñ merī zanjīreñ \\ na jaane kyā mire dīvār-o-bām kahte haiñ ',
 'tumhārī har nazar se munsalik hai rishta-e-hastī \\ magar ye duur kī bāteñ koī nādān kyā samjhe ',
 'tumhārī yaad ke jab zaḳhm bharne lagte haiñ \\ kisī bahāne tumheñ yaad karne lagte haiñ ',
 'tū jo mil jaa.e to taqdīr nigūñ ho jaa.e \\ yuuñ na thā maiñ ne faqat chāhā thā yuuñ ho jaa.e',
 'tū ne dekhī hai vo peshānī vo ruḳhsār vo hoñT \\ zindagī jin ke tasavvur meñ luTā dī ham ne',
 'uTh kar to aa gae haiñ tirī bazm se magar \\ kuchh dil hī jāntā hai ki kis dil se aae haiñ ',
 'udhar ek harf ki kushtanī yahāñ laakh uzr thā guftanī \\ jo kahā to sun ke uḌā diyā jo likhā to paḌh ke miTā diyā ',
 'ummīd-e-talattuf meñ ranjīda rahe donoñ \\ tū aur tirī mahfil maiñ aur mirī tanhāī ',
 'umr guzregī imtihān meñ kyā \\ daaġh hī deñge mujh ko daan meñ kyā ',
 'un kā āñchal hai ki ruḳhsār ki pairāhan hai \\ kuchh to hai jis se huī jaatī hai chilman rañgīñ',
 "vahī chashma-e-baqā thā jise sab sarāb samjhe \\ vahī ḳhvāb mo'tabar the jo ḳhayāl tak na pahuñche ",
 'vahī phir mujhe yaad aane lage haiñ \\ jinheñ bhūlne meñ zamāne lage haiñ ',
 'vahīñ haiñ dil ke qarāin tamām kahte haiñ \\ vo ik ḳhalish ki jise terā naam kahte haiñ ',
 'vo ahd-e-ġham kī kāhish-hā-e-be-hāsil ko kyā samjhe \\ jo un kī muḳhtasar rūdād bhī sabr-āzmā samjhe ',
 'vo jo ab chaak garebāñ bhī nahīñ karte haiñ \\ dekhne vaalo kabhī un kā jigar to dekho ',
 'vo mire ho ke bhī mire na hue \\ un ko apnā banā ke dekh liyā ',
 'vo nazar baham na pahuñchī ki muhīt-e-husn karte \\ tirī diid ke vasīle ḳhad-o-ḳhāl tak na pahuñche ',
 'vo rañg hai imsāl gulistāñ kī fazā kā \\ ojhal huī dīvār-e-qafas hadd-e-nazar se ',
 'vo to vo hai tumheñ ho jāegī ulfat mujh se \\ ik nazar tum mire mahbūb-e-nazar to dekho ',
 'vo tīrgī hai rah-e-butāñ meñ charāġh-e-ruḳh hai na sham-e-vāda \\ kiran koī aarzū kī laao ki sab dar-o-bām bujh gae haiñ ',
 'yaad kā phir koī darvāza khulā āḳhir-e-shab \\ dil meñ bikhrī koī ḳhushbu-e-qabā āḳhir-e-shab ',
 'yaar āshnā nahīñ koī Takrāeñ kis se jaam \\ kis dil-rubā ke naam pe ḳhālī subū kareñ ',
 'yahāñ vābastagī vaañ barhamī kyā jāniye kyuuñ hai \\ na ham apnī nazar samjhe na ham un kī adā samjhe ',
 'yahī kanār-e-falak kā siyah-tarīñ gosha \\ yahī hai matla-e-māh-e-tamām kahte haiñ ',
 'yak jaan na ho sakiye anjān na ban sakiye \\ yuuñ TuuT gaī dil meñ shamshīr-e-shanāsāī ',
 'ye aarzū bhī baḌī chiiz hai magar hamdam \\ visāl-e-yār faqat aarzū kī baat nahīñ',
 'ye ajab qayāmateñ haiñ tire rahguzar meñ guzarāñ \\ na huā ki mar miTeñ ham na huā ki jī uTheñ ham ',
 'ye bhī haiñ aise ka.ī aur bhī mazmūñ hoñge \\ lekin us shoḳh ke āhista se khulte hue hoñT',
 'ye chāheñ to duniyā ko apnā banā leñ \\ ye āqāoñ kī haDDiyāñ tak chabā leñ',
 'ye galiyoñ ke āvāra be - kār kutte \\ ki baḳhshā gayā jin ko zauq - e - gadā.ī',
 'ye har ek kī Thokareñ khāne vaale \\ ye fāqoñ se uktā ke mar jaane vaale',
 'ye har ik gaam pe un ḳhvāboñ kī maqtal-gāheñ \\ jin ke partav se charāġhāñ haiñ hazāroñ ke dimāġh',
 'ye har ik samt pur-asrār kaḌī dīvāreñ \\ jal-bujhe jin meñ hazāroñ kī javānī ke charāġh',
 'ye hasīñ khet phaTā paḌtā hai jauban jin kaa! \\ kis liye in meñ faqat bhuuk ugā kartī hai',
 'ye jafā-e-ġham kā chāra vo najāt-e-dil kā aalam \\ tirā husn dast-e-īsā tirī yaad rū-e-maryam ',
 'ye mazlūm maḳhlūq gar sar uThā.e \\ to insān sab sar - kashī bhuul jaa.e',
 'ye suḳhan jo ham ne raqam kiye ye haiñ sab varaq tirī yaad ke \\ koī lamha subh-e-visāl kā koī shām-e-hijr kī muddateñ ',
 'ye zid hai yaad harīfān-e-bāda-paimā kī \\ ki shab ko chāñd na nikle na din ko abr aae ',
 'yuuñ bahār aaī hai is baar ki jaise qāsid \\ kūcha-e-yār se be-nail-e-marām aatā hai ',
 'zahr se dho liye haiñ hoñT apne \\ lutf-e-sāqī ne jab kamī kī hai ',
 'zamāne kī phaTkār sarmāya in kā \\ jahāñ bhar kī dhutkār in kī kamā.ī',
 'zer-dastoñ ke masā.ib ko samajhnā sīkhā \\ sard aahoñ ke ruḳh-e-zard ke ma.anī sīkhe',
 'zikr-e-dozaḳh bayān-e-hūr o qusūr \\ baat goyā yahīñ kahīñ kī hai ',
 'ājizī sīkhī ġharīboñ kī himāyat sīkhī \\ yās-o-hirmān ke dukh-dard ke ma.anī sīkhe',
 'āshnā haiñ tire qadmoñ se vo rāheñ jin par \\ us kī mad.hosh javānī ne ināyat kī hai',
 'āshob-e-nazar se kī ham ne chaman-ārāī \\ jo shai bhī nazar aaī gul-rañg nazar aaī ',
 'ḳhāk-bar-sar chalo ḳhūñ-ba-dāmāñ chalo \\ raah taktā hai sab shahr-e-jānāñ chalo',

 'shām-e-firāq ab na pūchh aa.ī aur aa ke Tal ga.ī \\ dil thā ki phir bahal gayā jaañ thī ki phir sambhal ga.ī ',
 'bazm-e-ḳhayāl meñ tire husn kī sham.a jal ga.ī \\ dard kā chāñd bujh gayā hijr kī raat Dhal ga.ī ',
 'jab tujhe yaad kar liyā sub.h mahak mahak uThī \\ jab tirā ġham jagā liyā raat machal machal ga.ī ',
 'dil se to har mo.āmla kar ke chale the saaf ham \\ kahne meñ un ke sāmne baat badal badal ga.ī ',
 "āḳhir-e-shab ke ham-safar 'faiz' na jaane kyā hue \\ rah ga.ī kis jagah sabā sub.h kidhar nikal ga.ī ",

 "bām-e-mīnā se māhtāb utre \\ dast-e-sāqī meñ āftāb aa.e ",
 "har rag-e-ḳhūñ meñ phir charāġhāñ ho \\ sāmne phir vo be-naqāb aa.e ",
 "umr ke har varaq pe dil kī nazar \\ terī mehr-o-vafā ke baab aa.e ",
 "na ga.ī tere ġham kī sardārī \\ dil meñ yuuñ roz inqalāb aa.e ",
 "jal uThe bazm-e-ġhair ke dar-o-bām \\ jab bhī ham ḳhānumāñ-ḳharāb aa.e ",
 "is tarah apnī ḳhāmushī gūñjī \\ goyā har samt se javāb aa.e ",
 "'faiz' thī raah sar-ba-sar manzil \\ ham jahāñ pahuñche kāmyāb aa.e "]


# defining a function to read the most recent tweet_id

# def read_last_seen(FILE_NAME):
#     file_read = open(FILE_NAME, 'r')
#     last_seen_id = int(file_read.read().strip())
#     file_read.close()
#     return last_seen_id
#
#
# # defining a function to write the most recent tweet_id
#
# def store_last_seen(FILE_NAME, last_seen_id):
#     file_write = open(FILE_NAME, 'w')
#     file_write.write(str(last_seen_id))
#     file_write.close()
#     return
#
#
# # defining the main reply function
#
#
# def reply():
#     tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
#     for tweet in reversed(tweets):
#         random_verse = ' - ' + lyrics[randint(0, len(lyrics))]
#         mention_plus_username = '@' + tweet.user.screen_name
#         print(str(tweet.id), '-', tweet.full_text)
#         api.update_status(mention_plus_username + random_verse, tweet.id)
#         store_last_seen(FILE_NAME, tweet.id)

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
