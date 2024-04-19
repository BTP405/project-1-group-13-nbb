FROM python:3.9-slim
WORKDIR /Users/joshuadinham/repos/project-1-group-13-nbb
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 80

# ENTRYPOINT ["streamlit", "run", "./video_viewer.py", "--server.port=8501", "--server.address=0.0.0.0"]

CMD ["sh", "-c", "streamlit run --browser.serverAddress 0.0.0.0 --server.enableCORS False --server.port 80 /Users/joshuadinham/repos/project-1-group-13-nbb/video_viewer.py" ]