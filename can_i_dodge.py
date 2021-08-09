from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField,TextField,
                    TextAreaField, SubmitField)
#데이터의 유효성을 검사합니다. DataRequired를 이용하면 form의 그 항목의 데이터가 없을때 오류메세지를 보냅니다.
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOA'

class InfoForm(FlaskForm):

    #choice의 앞에 것이 세션을 통해 submission으로 넘어간다. 뒤에꺼는 label로 활용된다.
    #즉, 뒤는 보여주는 값 앞이 넘어가는 값이다.
    #형식은 동일하다 .무엇.필드(.묻는내용., .함수명.=[])

    double_lose = RadioField("2연패 이상인 사람이 있나요?", 
                        choices=[(-1,'그렇다.'), (0,'아니다.')])
    no_posi = RadioField("최근 10판 중에 그 포지션이 아닌 사람이 있나요?", 
                        choices=[(-1,'그렇다.'), (0,'아니다.')])
    lose_rate = RadioField("승률이 45% 미만인 사람이 있나요?", 
                        choices=[(-1,'그렇다.'), (0,'아니다.')])
    win_rate = RadioField("승률이 60% 이상인 사람이 있나요?", 
                        choices=[(1,'그렇다.'), (0,'아니다.')])

    no_cc = RadioField("2연패 이상인 사람이 있나요?", 
                        choices=[(-2,'그렇다.'), (0,'아니다.')])
    no_deal = RadioField("광역딜이 없나요?", 
                        choices=[(-2,'그렇다.'), (0,'아니다.')])
    all_ad = RadioField("올 ad 인가요?", 
                        choices=[(-1,'그렇다.'), (0,'아니다.')])
    all_ap = RadioField("올 ap 인가요?", 
                        choices=[(-2,'그렇다.'), (0,'아니다.')])

    win_lane = RadioField("내 라인이 이기는 상성인가요?", 
                        choices=[(1,'그렇다.'), (0,'아니다.')])
    bad_vscomp = RadioField("적 조합이 안좋은가요?", 
                        choices=[(1,'그렇다.'), (0,'아니다.')])
                                                                                                                                                                                                    
    submit = SubmitField('결과보기')
    
@app.route('/', methods=['GET','POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['double_lose'] = int(form.double_lose.data)
        session['no_posi'] = int(form.no_posi.data)
        session['lose_rate'] = int(form.lose_rate.data)
        session['win_rate'] = int(form.win_rate.data)
        session['no_cc'] = int(form.no_cc.data)
        session['no_deal'] = int(form.no_deal.data)
        session['all_ad'] = int(form.all_ad.data)
        session['all_ap'] = int(form.all_ap.data)
        session['win_lane'] = int(form.win_lane.data)
        session['bad_vscomp'] = int(form.bad_vscomp.data)
        
        session['result'] = session['double_lose'] + session['no_posi'] + session['lose_rate'] + session['win_rate'] + session['no_cc'] + session['no_deal'] + session['all_ad'] + session['all_ap'] + session['win_lane'] + session['bad_vscomp']

        return redirect(url_for('submission'))

    return render_template('home.html', form=form)

@app.route('/submission')
def submission():
    return render_template('submission.html')


if __name__ == '__main__':
    app.run(debug=True)
        
    