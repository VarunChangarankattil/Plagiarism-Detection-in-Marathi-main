import stanza
import streamlit as st
from streamlit_option_menu import option_menu

stanza.download('mr')
nlp = stanza.Pipeline('mr')
# doc1 = nlp("पण खुप जण ह्या क्षेत्रातनवीन असल्यामुळे त्यांना प्लँगँरिझम म्हणजे काय? हेच माहीत नसते. मग ते प्लँगँरिझम चेक तरी कसा करणार.")
# doc2 = nlp("पण खुप जण ह्या क्षेत्रात नवीन असल्यामुळे त्यांना प्लँगँरिझम म्हणजे काय? हेच माहीत नसते. मग ते प्लँगँरिझम चेक तरी कसा करणार.")
# doc2 = nlp(" पण खुप जण ह्या क्षेत्रात नवीन असल्यामुळे त्यांना प्लँगँरिझम म्हणजे काय? हेच माहीत नसते. मग ते प्लँगँरिझम चेक तरी कसा करणार.")


EXAMPLE_NO = 1


def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Plagiarism Detector Tool", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Plagiarism Detector Tool", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Plagiarism Detector Tool", "Contact"],
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    # st.title(f"You have selected {selected}")
    col1, col2 = st.columns([7, 5])

    with col1:
        st.title("What is Plagiarism?")
        st.write("Plagiarism is basically reusing someone’s work, ideas, results, or words without giving credit to "
                 "the original writer and source. Today, plagiarism is a very testing issue in the field of education "
                 "and journalism/ print media.")

    with col2:
        st.write("")
        st.write("")
        st.write("")
        st.image('./plag.svg')

    st.title("Why Use a Plagiarism Checker?")
    st.write("You’re working on a paper and you’ve just written a line that seems kind of familiar. Did you read it "
             "somewhere while you were researching the topic? If you did, does that count as plagiarism? Now that "
             "you’re looking at it, there are a couple of other lines that you know you borrowed from somewhere. You "
             "didn’t bother with a citation at the time because you weren’t planning to keep them. But now they’re an "
             "important part of your paper. Is it still plagiarism if you’re using less than a paragraph?")
    st.write('')
    st.write(" Using "
             "someone else’s text without attribution is plagiarism, whether you meant to do it or not. Unintentional "
             "plagiarism of even a sentence or two can have serious consequences. For students, plagiarism often "
             "means a failing grade, academic probation, or worse. ")

    st.title("Why Originality & Uniqueness of Content Matters?")
    col3, col4 = st.columns([5, 7])
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.image("./ugun.svg")

    with col4:
        st.write("Content is the most crucial element of a website as it decides whether it will help a website earn "
                 "a high position in search engines and attract visitors or not. Attracting customers and search "
                 "engines isn’t a piece of cake as your site’s content needs to be of high quality. One of the "
                 "essential traits of high-quality content is originality, and it will determine its rank on search "
                 "engine result pages.")
        st.write("")
        st.write("If your content is plagiarized with already available information on the web, then your site will "
                 "get hurt, and its position on search results will drastically fall sooner or later. On the other "
                 "hand, the uniqueness of content will give people a reason to choose your site over others in this "
                 "competitive environment. If you’re facing such problems and want to get rid of this nuisance, "
                 "then a simple way out is to use our plagiarism software.")

if selected == "Plagiarism Detector Tool":
    st.title("Marathi plagiarism detection")
    line1 = st.text_input('Corpus 1')
    line2 = st.text_input('Corpus 2')

    doc1 = nlp(line1)
    doc2 = nlp(line2)

    sent1_l = []
    sent1_ll = []

    # print(doc1)
    # print(*[f'{word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')
    for sent in doc1.sentences:
        for word in sent.words:
            sent1_l = word.lemma
            sent1_ll.append(sent1_l)

    sent2_l = []
    sent2_ll = []

    for sent in doc2.sentences:
        for word in sent.words:
            sent2_l = word.lemma
            sent2_ll.append(sent2_l)

    # st.write("\nLemma of sentence 1:")
    # st.write(sent1_ll)
    # st.write("\nLemma of sentence 1:")
    # st.write(sent2_ll)

    stopwords_mr = ['अधिक', 'अनेक', 'अशी', 'असलयाचे', 'असलेल्या', 'असा', 'असून', 'असे', 'आज', 'आणि', 'आता', 'आपल्या',
                    'आला',
                    'आली', 'आले', 'आहे', 'आहेत', 'एक', 'एका', 'कमी', 'करणयात', 'करून', 'का', 'काम', 'काय', 'काही',
                    'किवा',
                    'की', 'केला', 'केली', 'केले', 'कोटी', 'गेल्या', 'घेऊन', 'जात', 'झाला', 'झाली', 'झाले', 'झालेल्या',
                    'टा',
                    'डॉ', 'तर', 'तरी', 'तसेच', 'ता', 'ती', 'तीन', 'ते', 'तो', 'त्या', 'त्याचा', 'त्याची', 'त्याच्या',
                    'त्याना', 'त्यानी', 'त्यामुळे', 'त्री', 'दिली', 'दोन', 'न', 'नाही', 'निर्ण्य', 'पण', 'पम', 'परयतन',
                    'पाटील', 'म', 'मात्र', 'माहिती', 'मी', 'मुबी', 'म्हणजे', 'म्हणाले', 'म्हणून', 'या', 'याचा', 'याची',
                    'याच्या', 'याना', 'यानी', 'येणार', 'येत', 'येथील', 'येथे', 'लाख', 'व', 'व्यकत', 'सर्व', 'सागित्ले',
                    'सुरू', 'हजार', 'हा', 'ही', 'हे', 'होणार', 'होत', 'होता''होती', 'होते', '. ', ', ', '.', ','
                    ]

    l1 = [];
    l2 = []

    # remove stop words from the string
    X_set = {w for w in sent1_ll if not w in stopwords_mr}
    Y_set = {w for w in sent2_ll if not w in stopwords_mr}

    # st.write('\nRemoving stopwords:')
    # st.write("Sent 1: ")
    # st.write(X_set)
    # st.write("Sent 2: ")
    # st.write(Y_set)

    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]

    import time

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)

    st.write("")
    st.write("")

    if c != 0:
        cosine = (c / float((sum(l1) * sum(l2)) ** 0.5)) * 100
        cosine = "{:.2f}".format(cosine)
        st.title("Result")
        st.write("Plagiarism:  ", cosine, '%')

if selected == "Contact":
    st.title(f"You have selected {selected}")
