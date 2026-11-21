
import streamlit as st
from assistant import troubleshoot



st.set_page_config(
    page_title="AI Troubleshooting Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

st.markdown("""
<style>

/* Main application */

.stApp {
    background-color: #0b1120;
    color: #e2e8f0;
}

.block-container {
    padding-top: 3rem;
    max-width: 1100px;
}

[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #263449;
}

/* Sidebar title */

.sidebar-title {
    font-size: 21px;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.5;
    padding-top: 5px;
}

/* Baseline under sidebar title */

.sidebar-baseline {
    width: 100%;
    height: 1px;
    background-color: #344155;
    margin-top: 18px;
    margin-bottom: 24px;
}

/* Sidebar section heading */

.sidebar-section {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 16px;
}

/* Fixed Clear Conversation button */

[data-testid="stSidebar"] div[data-testid="stButton"] {
    position: fixed;
    bottom: 18px;
    left: 16px;
    width: 280px;
    z-index: 999;
}

/* Sidebar button styling */

[data-testid="stSidebar"] div[data-testid="stButton"] button {
    background-color: #17243a;
    border: 1px solid #344155;
    color: #cbd5e1;
    border-radius: 10px;
    min-height: 44px;
    text-align: center;
}

[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background-color: #263449;
    border-color: #60a5fa;
    color: white;
}


.main-title {
    font-size: 34px;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 8px;
}

.main-description {
    color: #94a3b8;
    font-size: 16px;
    margin-bottom: 35px;
}

/* Sample issue heading */

.section-label {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin: 25px 0 12px 0;
}


div[data-testid="stChatMessage"] {
    background-color: #151f31;
    border: 1px solid #29364c;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 12px;
}

div[data-testid="stChatInput"] {
    border-color: #334155;
}

.stButton > button {
    background-color: #17243a;
    color: #dbeafe;
    border: 1px solid #344765;
    border-radius: 10px;
    text-align: left;
    min-height: 48px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background-color: #243b63;
    border-color: #60a5fa;
    color: white;
}


div[data-testid="stExpander"] {
    background-color: #151f31;
    border: 1px solid #29364c;
    border-radius: 10px;
}

hr {
    border-color: #263449;
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size: 21px;
            font-weight: 700;
            color: #f1f5f9;
            line-height: 1.5;
            padding-top: 5px;
        ">
            🤖 AI Troubleshooting Assistant
        </div>

        <div style="
            color: #94a3b8;
            font-size: 12px;
            line-height: 1.6;
            margin-top: 5px;
            margin-bottom: 22px;
        ">
            Intelligent troubleshooting for support engineers
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-section">HOW TO USE</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div style="display:flex; gap:12px; margin-bottom:20px;">
        <span style="color:#60a5fa; font-weight:700;">01</span>
        <span style="color:#cbd5e1; font-size:14px;">
            Describe your technical issue
        </span>
    </div>

    <div style="display:flex; gap:12px; margin-bottom:20px;">
        <span style="color:#60a5fa; font-weight:700;">02</span>
        <span style="color:#cbd5e1; font-size:14px;">
            Get relevant troubleshooting steps
        </span>
    </div>

    <div style="display:flex; gap:12px;">
        <span style="color:#60a5fa; font-weight:700;">03</span>
        <span style="color:#cbd5e1; font-size:14px;">
            Follow guidance or escalate
        </span>
    </div>
    """, unsafe_allow_html=True)


    # Clear conversation button
    if st.button(
        "🗑️  Clear conversation",
        use_container_width=True,
        key="clear_conversation"
    ):
        st.session_state.messages = []
        st.session_state.pending_question = None
        st.rerun()


st.markdown(
    '<div class="main-title">How can I help you?</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-description">'
    'Describe your technical issue to get troubleshooting guidance.'
    '</div>',
    unsafe_allow_html=True
)

if not st.session_state.messages:

    st.markdown(
        '<div class="section-label">TRY A SAMPLE ISSUE</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💳  Payment API returning HTTP 500",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "My payment API is returning a 500 error"
            )
            st.rerun()

        if st.button(
            "🗄️  Database connection failure",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "I am unable to connect to the database"
            )
            st.rerun()

    with col2:

        if st.button(
            "🔐  OTP not received",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "I am not receiving my OTP"
            )
            st.rerun()

        if st.button(
            "⚙️  Server CPU utilization is high",
            use_container_width=True
        ):
            st.session_state.pending_question = (
                "The server CPU utilization is very high"
            )
            st.rerun()


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander("📚 View knowledge sources"):

                    for source in sources:
                        st.markdown(
                            f"**{source['id']}** — {source['issue']}"
                        )

            else:
                st.caption(
                    "No sufficiently relevant knowledge source found."
                )


user_question = st.chat_input(
    "Describe your technical issue..."
)

if user_question:
    st.session_state.pending_question = user_question


if st.session_state.pending_question:

    question = st.session_state.pending_question
    st.session_state.pending_question = None

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching knowledge base and investigating..."
        ):

            try:

                result = troubleshoot(question)

                # Display response progressively
                answer = st.write_stream(
                    result["answer_stream"]
                )

                sources = result["sources"]

                if sources:

                    with st.expander(
                        "📚 View knowledge sources",
                        expanded=True
                    ):

                        for source in sources:
                            st.markdown(
                                f"**{source['id']}** — {source['issue']}"
                            )

                else:
                    st.warning(
                        "No sufficiently relevant knowledge source found. "
                        "Please provide additional information."
                    )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as error:

                error_message = (
                    "I encountered an error while processing your request. "
                    "Please try again."
                )

                print("Application Error:", error)

                st.error(error_message)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message,
                    "sources": []
                })
