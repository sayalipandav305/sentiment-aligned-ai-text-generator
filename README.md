# Sentiment-Aligned AI Text Generator

This project leverages advanced natural language processing (NLP) techniques to generate text that aligns with specified sentiment tones. By integrating sentiment analysis with text generation models, it enables the creation of content that conveys desired emotional undertones.

## 🚀 Features

* **Sentiment-Driven Text Generation**: Generate text that embodies specific sentiments such as positive, negative, or neutral.
* **Streamlit Interface**: A user-friendly web interface for real-time interaction with the model.
* **Customizable Sentiment Inputs**: Users can specify the desired sentiment to guide the text generation process.

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/sayalipandav305/sentiment-aligned-ai-text-generator.git
cd sentiment-aligned-ai-text-generator
```

### Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## 🧪 Usage

### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

Navigate to `http://localhost:8501` in your web browser to interact with the application.

### Command-Line Interface (Optional)

For generating sentiment-aligned text via the command line:

```bash
python sentiment_and_generation.py --sentiment "positive" --input_text "I am feeling great today"
```

Replace `"positive"` with your desired sentiment and provide the input text accordingly.

## 📄 File Descriptions

* `streamlit_app.py`: The main application file that launches the Streamlit interface.
* `sentiment_and_generation.py`: Script for generating sentiment-aligned text based on user input.
* `requirements.txt`: Lists the necessary Python packages for the project.

## 📚 Dependencies

Ensure the following packages are installed:

* `streamlit`
* `transformers`
* `torch`
* `nltk`
* `pandas`

These can be installed via the `requirements.txt` file.

## 📌 Notes

* The model's performance may vary based on the complexity and length of the input text.
* For optimal results, provide clear and concise input prompts.
* The sentiment alignment is achieved through fine-tuning pre-trained language models with sentiment-specific datasets.

## 🛠️ Development Setup

To contribute to the development of this project:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request to the main repository.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

