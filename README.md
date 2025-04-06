# fastapi-react-template
FastAPI+React+DB(MySQL,Redis)
https://docs.astral.sh/uv/guides/integration/fastapi/#migrating-an-existing-fastapi-project



npm create vite@latest frontend -- --template react
cd frontend
npm install

pacage.jsonを以下のように修正
  "scripts": {
    "dev": "vite --host",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },

  npm run dev