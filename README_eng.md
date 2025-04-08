# Examples of themes addressed by media art related to "water" in a "experiential" format within MADB.

## 1. Theme Explanation
I am interested in media art and, in the future, would like to organize or assist in organizing such events. Specifically, I am considering works related to the beautiful theme of "water," and more importantly, those that involve an interactive experience for participants. Therefore, in this analysis, I aim to clarify the contexts and intentions in which past "water"-related "experiential" media art works have been held, based on data collected within the MADB. By examining specific examples of past works, I can ensure the novelty and uniqueness of future media art projects.
2. Analysis 1: Media Art Works with Words Related to "Water" in Their Titles or Descriptions
## 2.1 Target of Analysis
Type: Media Art (Media Art Events, Exhibitions, and Performances)

### 2.2 Analysis Method
I will extract media art works from the MADB where the title or description contains words related to "water," such as "水," "water," "ウォーター" (water in Japanese), and "ウオーター" (water in Japanese). The term "water-related media art" refers to works whose labels or descriptions contain the above words. Note that terms like "みず" or "ミズ" are not considered to mean "water" in this context, and are excluded. Additionally, other terms that indirectly express liquid water are not considered and thus excluded.

### 2.3 Data Acquisition and Organization Method
For data collection, I will use SPARQL queries to filter media art events and exhibitions/performances, targeting those that include water-related terms in their labels and genres. Further, I will hypothesize and verify how "water" is used in the context of these works. MeCab will be used to list the frequency and occurrence of the words outlined in 2.8, and from this, I will verify whether the background and intention of how "water" is used align with my hypothesis and examine the trends in the themes.

### 2.4 Results I
Query: [sparql/sparql1.rq](sparql/spqrql1.rq)

### 2.5 Hypothesis Based on Results I
I hypothesize the following words will appear frequently based on the context of "water":

① Environment, nature, pollution, drought, thirst
Environmental issues related to water have become a major concern in recent years, often explored through various media. Particularly, media art tends to satirically address contemporary social problems more than other art forms. Thus, when media art uses the word "water," it is likely to refer to environmental issues.

② Biology, absorption, excretion
Living beings, including humans, cannot survive without water. However, despite its importance, we rarely acknowledge its presence. This may reflect the growing trend of bio-art, where living organisms are used in creative expression. Thus, media art may suggest the relationship between water and life.

③ Physics, liquid, motion, density, dissolution
Water possesses unique properties compared to other substances. For example, it is rare for a solid to have a lower density than its liquid form. Additionally, the latent heat of fusion for ice is approximately 80 times larger than its specific heat. Media art is adept at expressing these physical properties and raising awareness about them.

### 2.6 Verification of Hypothesis Results II
I will refine the results from Results I by further searching for the hypothesized keywords, narrowing down the results. By examining the actual search results, I will assess whether the hypothesis holds, and discuss my findings in 2.7, Consideration I.
① "Environment": 28/207, "Nature": 18/207, "Pollution": 2/207, "Drought": 0/207, "Thirst": 0/207
② "Biology": 9/207, "Absorption": 0/207, "Excretion": 1/207
③ "Physics": 9/207, "Liquid": 2/207, "Motion": 8/207, "Density": 0/207, "Dissolution": 0/207

### 2.7 Consideration I Based on Results I and II
The hypothesis aligns quite well with the results for works that focus on environmental issues. In particular, the use of "environment" within the context of water-related works was mostly related to environmental problems. However, there were few works that directly pointed to specific issues like water pollution or resource depletion. Instead, the relationship between water and the environment was often explored in an abstract manner, prompting viewers to consider it conceptually through art. This suggests that media art is not necessarily a platform for practical, actionable proposals, but rather one that appeals to the senses and conveys abstract messages.

The number of works that include terms related to "biology" and "physics" were fewer than those focused on "environment." Additionally, even fewer works explicitly explained how specific technologies or methods were used to represent biology or physics. This may be due to the fact that media art is not primarily about showcasing scientific or technological principles, but rather about using those elements to communicate the creator's artistic sensibilities and messages.

Furthermore, the number of works related to "biology" or "physics" remained the same whether we searched with just the term "water" (188 results) or with the additional water-related terms (207 results). This suggests that when works deal with "biology" or "physics," the word "water" is often directly used, rather than using terms like "water" or "ウォーター."

### 2.8 Results III
Next, I will examine which other nouns were most frequently used in proximity to the words "water," "ウォーター," or "ウオーター" by analyzing them with MeCab. I will list them in order of frequency of occurrence.

MeCab Results
I will check the nouns that appeared most often alongside "water" and similar terms and list them by frequency.
Result:[data/word_count1.csv](data/word_count1.csv)


### 2.9 Consideration II Based on Results III
The most frequent words tend to refer to operational aspects, such as time and event organization. However, there are also nouns that provide clues about the themes and intentions of the works. In particular, terms like "video" (126), "sound" (102), "music" (64), and "performance" (52) suggest that many works utilized video and sound. In these cases, "water" was not necessarily the central theme, but rather appeared metaphorically in relation to video and sound. An example is: "In the center of the work, the dark water surface is dotted with water drops, and ripples spread out, while delicate sounds envelop the venue in response" (water state 1 / "water state 1" @en, Yamaguchi Center for Arts and Media [YCAM], Media Art Database, 2024.08.09 confirmed).

## 3. Analysis 2: Media Art Including "Experience" or "Participation" in Titles or Descriptions

### 3.1 Analysis Target
Type: Media Art (Media Art Events, Media Art Exhibitions/Performances)

### 3.2 Analysis Method
Extract items from the Media Arts Database (MADB) where the title or description includes "体験" ("experience") or "参加" ("participation"). Label works as "Experiential Media Art" if the title or description contains these terms.

### 3.3 Data Acquisition and Organization Method
Following the same approach as in Analysis 1, data is retrieved using SPARQL queries targeting media art events and exhibitions/performances. The queries filter for items where the label or genre includes "体験" ("experience") or "参加" ("participation"). Additionally, hypotheses are formulated and tested to understand the context in which these terms are used within the works. Terms listed in section 3.8 and their frequent co-occurring words are analyzed using MeCab to enumerate their occurrences. The goal is to verify whether the usage context of these terms aligns with the hypotheses and to identify thematic trends.

### 3.4 Result I
Query: [sparql/sparql2.rq](sparql/spqrql2.rq)

### 3.5 Hypotheses Based on Result I

Formulate hypotheses regarding the intent behind the use of "体験" ("experience") and "参加" ("participation"). The following terms are expected to frequently co-occur:

Sensation, Perception, Sense, Feeling: Experiencing art inherently involves stimulating the five senses such as sight and hearing. It is considered mainstream to enhance these stimuli through scientific technology.​

Movement, Motion: With the rise of interactive art responding to participants' movements, it is anticipated that many works include the term "運動" ("movement") in their descriptions. Participants' movements reflected in the artwork can impart unique value and significance as records.

### 3.6 Hypothesis Testing - Result II

Further search the keywords mentioned in the hypotheses within Result I to refine the findings. Observe the actual search results to assess the validity of the hypotheses, which will be discussed in section 3.7.

"感覚" ("sensation"): 60 occurrences out of 821

"知覚" ("perception"): 22/821

"感" ("sense") and "覚" ("feeling"): 166/821 each

"運動" ("movement"): 29/821

"動" ("motion"): 273/821

### 3.7 Consideration I Based on Results I and II

Terms related to "感覚" ("sensation") were frequently used in descriptions of works aiming to heighten awareness of the five senses, aligning with the hypothesis. Many works intended to sharpen visual and auditory senses using imagery and sound. Additionally, "ゲーム感覚" ("game-like sensation") and "本の中に入ったような感覚" ("sensation of entering a book") were used metaphorically.​

The number of works containing "運動" ("movement") was lower than hypothesized. However, in most cases, the intent of participants "experiencing" through "movement" matched the hypothesis. For example, an event offered participants the opportunity to experience the benefits of "Gyrokinesis," a dance form derived from yoga for dancers.​

Regarding "動" ("motion"), it was used in diverse contexts beyond "運動" ("movement"), including "振動" ("vibration"), "(身体の)動き" ("(body) movement"), and "(アニメーションの)動き" ("(animation) motion").

### 3.8 Result III

To identify the actual nouns that co-occurred with terms related to "感覚" ("sensation") and "運動" ("movement"), morphological analysis was conducted using MeCab. The nouns were listed in order of frequency. The results are available at:​
Result:[data/word_count2.csv](data/word_count2.csv)

### 3.9 Consideration II Based on Result III

The basic trends align with those observed when examining terms related to "水" ("water") and frequently co-occurring words. Terms like "映像" ("image") (323 occurrences), "音" ("sound") (285), and "サウンド" ("sound") (81) appeared frequently. Similar to Analysis I, "映像" ("image") appeared more frequently than "音" ("sound") or "音響" ("acoustics") (121), suggesting a prevalence of works focusing on visual stimulation over auditory.​

A notable difference from Analysis I is the frequent occurrence of academic terms such as "研究" ("research") (127), "技術" ("technology") (111), and "開発" ("development") (99). This suggests that in works aiming to make participants re-recognize their "感覚" ("senses") through "体験" ("experience"), the underlying "技術" ("technology") plays a more significant role compared to works involving "水" ("water").​

## 4. Analysis 3: Media Art Including Terms Related to "Water" and "Experience" in Titles or Descriptions

### 4.1 Analysis Target
Type: Media Art (Media Art Events, Media Art Exhibitions/Performances)

### 4.2 Analysis Method
Extract items from MADB where the title or description includes terms related to "水" ("water")—such as "水" ("water"), "water," "ウォーター" ("water"), or "ウオーター" ("water")—and "体験" ("experience") or "参加" ("participation").

### 4.3 Data Acquisition and Organization Method
Following the same approach as in Analyses 1 and 2, data is retrieved using SPARQL queries targeting media art events and exhibitions/performances. The queries filter for items where the label or genre includes terms related to "水" ("water") and "体験" ("experience") or "参加" ("participation"). Additionally, hypotheses are formulated and tested to understand the context in which these terms are used within the works. Terms listed in section 4.8 and their frequent co-occurring words are analyzed using MeCab to enumerate their occurrences. The goal is to verify whether the usage context of these terms aligns with the hypotheses and to identify thematic trends.

### 4.4 Result I
Query: [sparql/sparql3.rq](sparql/spqrql3.rq)

### 4.5 Consideration I Based on Result I
Environment, Nature: Many media art works may aim to make participants realize and address environmental issues related to "水" ("water") through "体験" ("experience"). In Analysis
