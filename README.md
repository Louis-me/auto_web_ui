# ˵��
- ���docker-selenium��pytest���зֲ�ʽ�Ĳ���
- ����̿��Բο�[����](http://www.shikun.work/aposts/d8b0934a/)

## ִ��

- ֱ���������� 
```buildoutcfg
pytest -s testcase/��ع�/С�ع�/ð�� -n 3 --html=report.html --self-contained-html --capture=sys
```

- ����runner.py�д���
```buildoutcfg
    pytest.main(['%s' %path,'-n 3', '--html=report.html','--self-contained-html', '--capture=sys'])

```

- ��ִ�е�ÿ������
- ִ��ʧ�ܺ��ͼ
![](img/1.PNG)