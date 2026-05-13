from flask import Flask, render_template, request, send_file
from scrapper import search_incruit
from file import save_to_csv
# from scrapper import search_incruit, search_saramin # 함수 추가 임포트

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    # print(keyword)
    search_incruit(keyword, 1)
    jobs = search_incruit(keyword, 1)

    return render_template("search.html", jobs= enumerate(jobs), keyword=keyword)

@app.route("/file")
def file():
    keyword = request.args.get("keyword")
    jobs = search_incruit(keyword, 1)
    save_to_csv(jobs)
    return send_file("downloads.csv", as_attachment=True)

# @app.route("/search")
# def search():
#     keyword = request.args.get("keyword")

#     # 두 사이트의 결과를 모두 가져와서 합칩니다.
#     incruit_jobs = search_incruit(keyword, 1)
#     saramin_jobs = search_saramin(keyword, 1)
    
#     # 리스트 두 개를 합쳐서 하나의 jobs 리스트로 만듭니다.
#     all_jobs = incruit_jobs + saramin_jobs

#     return render_template("search.html", jobs=enumerate(all_jobs), keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)