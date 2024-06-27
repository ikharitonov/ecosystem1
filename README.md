# ecosystem1

Iteration 0:
- Secure Access
- Initial simple login system and jobs posting support
- Local LLM Inference with GPU support
- Python web framework powered
- File Upload, Zip Upload
- Vectorisation, Metadata-powered embeddings
- Docker-run GROBID Internal Chunking Service
- Latent Space Visualisation, Manual Clustering for Fine-tuning
- 3D Visualisations with Contextual Information
- MySQL Database for Unique Chunk Listings (server-wide)
- Multiwindow Frontend for Flexible Workflows

Iteration 1:
- GROBID XML parsing
- GROBID REST API access to chunking
- Python script for accepting a zipped filesystem archive, unzipping and embedding
- Metadata powered embedding, use folder names as initial metadata
- MySQL database registering embedded chunks with unique IDs and locations to chunk content
- Web framework can injest files from user, pass them to and launch embedding scripts; display MySQL database contents on the website; launch dim. red. scripts
- 2D/3D visualisations of chunks in latent space

29/04/2024 Use Case 1:
- Datasets consist of pdf/word text files with diverse semantic content
- Uploaded datasets are scanned for directory structure and registered
- Implement Structure Elements
- A text summarisation model is then applied to each document
- Short summaries are converted to embeddings
- Dimensionality reduction is applied to embeddings
- Embedding projections are visualised in 2D/3D in the frontend, coloring is applied according to directory structure

Future implementation: Knowledge Graphs, reference allowed file type schema
