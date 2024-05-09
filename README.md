# ecosystem1

Secure Access: VPN network for users to access the domain name

Initial rudimentary login system and jobs posting support

GPU Support

Local LLM Inference

Frontend JS Backend Python

File Upload, Zip Upload

Vectorisation, Metadata-powered Embedding

Docker-run GROBID Internal Chunking Service

Latent Space Visualisation, Manual Clustering for Fine-tuning

3D Visualisations with Contextual Information

MySQL Database for Unique Chunk Listings (server-wide)

Multiwindow Frontend for Flexible Workflows

Iteration 1:
- write up GROBID XML parsing
- write up GROBID REST API access to chunking
- write up python script for accepting a zipped filesystem archive, unzipping and embedding
- look into metadata powered embedding, use folder names as initial metadata
- build a MySQL database registering embedded chunks with unique IDs and locations to chunk content
- construct a HTML+JS frontend that can talk to Python backend - can inject files from website, pass them to and launch embedding scripts; display MySQL database contents on the website; launch dim. red. scripts
- construct 2D/3D visualisations of chunks in latent space

29/04/2024:

Use Case 1:
- Datasets consist of pdf/word text files with diverse semantic content
- Uploaded datasets are scanned for directory structure and registered
- Implement Structure Elements
- A text summarisation model is then applied to each document
- Short summaries are converted to embeddings
- Dimensionality reduction is applied to embeddings
- Embedding projections are visualised in 2D/3D in the frontend, coloring is applied according to directory structure

Future implementation: Knowledge Graphs, reference allowed file type schema
