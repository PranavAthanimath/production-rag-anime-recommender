import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender",
                   layout="wide", page_icon="🎌")

load_dotenv()


@st.cache_resource
def init_pipeline():
    """Initialize the recommendation pipeline with caching"""
    return AnimeRecommendationPipeline()


# Initialize pipeline
try:
    pipeline = init_pipeline()
except Exception as e:
    st.error(f"Failed to initialize the recommendation system: {str(e)}")
    st.stop()

# Header
st.title("🎌 Anime Recommender System")
st.markdown("Get personalized anime recommendations powered by AI")

# Sidebar with example queries
with st.sidebar:
    st.header("💡 Example Queries")
    st.markdown("""
    Try these example queries:
    - Light-hearted anime with school settings
    - Dark fantasy anime with complex plot
    - Action anime with strong female lead
    - Slice of life anime about friendship
    - Sci-fi anime set in space
    """)

    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        "This system uses RAG (Retrieval-Augmented Generation) to recommend anime based on your preferences.")

# Main input
query = st.text_input(
    "What kind of anime are you looking for?",
    placeholder="e.g., light-hearted anime with school settings",
    help="Describe the type of anime you want - genres, themes, mood, setting, etc."
)

# Process query
if query:
    if len(query.strip()) < 3:
        st.warning(
            "⚠️ Please enter at least 3 characters for better recommendations")
    else:
        try:
            with st.spinner("🔍 Searching for the perfect anime recommendations..."):
                response = pipeline.recommend(query.strip())

            st.markdown("### 📺 Recommendations")
            st.markdown(response)

        except Exception as e:
            st.error(f"❌ Error generating recommendations: {str(e)}")
            st.info(
                "Please try rephrasing your query or check your API key configuration.")
else:
    # Show placeholder when no query
    st.info("👆 Enter your preferences above to get started!")
