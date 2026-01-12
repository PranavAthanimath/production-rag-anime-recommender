# 🎌 Production RAG Anime Recommender

AI-powered anime recommendation system built with **RAG (Retrieval-Augmented Generation)**, deployed on **Kubernetes**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

## 🎯 What It Does

Enter your anime preferences (e.g., "dark fantasy with complex plot") and get personalized recommendations powered by semantic search and LLM reasoning.

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Vector Database** | ChromaDB with HuggingFace embeddings |
| **LLM** | Groq API (Llama 3.1 8B) |
| **Orchestration** | LangChain (LCEL) |
| **Frontend** | Streamlit |
| **Containerization** | Docker |
| **Deployment** | Kubernetes (Minikube) |

## 📚 Learning Outcomes

By building this project, you'll learn:

### RAG Architecture
- How to build a production RAG pipeline from scratch
- Vector embeddings and semantic search concepts
- Prompt engineering for grounded responses

### LangChain & LLM Integration
- Modern LangChain Expression Language (LCEL)
- Connecting retrievers with LLMs
- Managing API keys securely with environment variables

### Containerization & Kubernetes
- Writing production Dockerfiles
- Kubernetes Deployments, Services, and Secrets
- Resource limits and health probes
- Debugging OOMKilled and CrashLoopBackOff errors

### MLOps/LLMOps
- End-to-end ML pipeline (data → embeddings → inference)
- Environment management with `uv`
- Git workflow for ML projects

## 🚀 Quick Start

### Local Development
```bash
# Clone the repo
git clone https://github.com/PranavAthanimath/production-rag-anime-recommender.git
cd production-rag-anime-recommender

# Create virtual environment
uv venv --python 3.11
.venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt -e .

# Set up environment
echo "GROQ_API_KEY=your-key-here" > .env

# Run the app
streamlit run app/app.py
```

### Kubernetes Deployment
```bash
# Start Minikube
minikube start

# Use Minikube's Docker
eval $(minikube docker-env)

# Build image
docker build -t anime-recommender:v1.0 .

# Create secret
kubectl create secret generic anime-secrets \
  --from-literal=GROQ_API_KEY=your-key

# Deploy
kubectl apply -f llmops-k8s.yaml

# Access the app
kubectl port-forward svc/anime-recommender-service 8501:80 --address 0.0.0.0
```

## 📁 Project Structure

```
├── app/app.py              # Streamlit UI
├── src/
│   ├── data_loader.py      # Data processing
│   ├── vector_store.py     # ChromaDB builder
│   ├── recommender.py      # RAG chain
│   └── prompt_template.py  # LLM prompts
├── pipeline/
│   ├── pipeline.py         # Main pipeline
│   └── build_pipeline.py   # Vector store builder
├── chroma_db/              # Pre-built vector database
├── Dockerfile              # Container config
├── llmops-k8s.yaml         # Kubernetes deployment
└── requirements.txt        # Dependencies
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `OOMKilled` | Increase memory in `llmops-k8s.yaml` to 2Gi |
| `ImagePullBackOff` | Build image with `eval $(minikube docker-env)` first |
| `Connection error` | Wait 2-3 min for pipeline init, add CORS flags to Dockerfile |

## 📄 License

MIT License - feel free to use for learning!

---

Built by [Pranav Athanimath](https://github.com/PranavAthanimath)
