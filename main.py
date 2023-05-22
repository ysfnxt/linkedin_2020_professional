import pandas as pd

df = pd.read_csv('file3.csv')
email_list = df['emails'].values.tolist()

no_of_emails = []
for i in email_list:
    if "professional"  or "None" in i:
        no_of_emails.append(i.count("professional")+i.count("None"))
    else:
        print('NA')

count = 0
prof_mail = []
for i,j in enumerate(email_list):
    b = email_list[i].split(',')
    for i,j in enumerate(b):
        if 'professional' in j or "None" in j:
            prof_mail.append(b[i-1].split(':')[1].replace("'",''))
            count += 1


count = 0
k = 0
for i in no_of_emails:
    email = ''
    for j in range(0,i):
        if i > 1:
            email = email + prof_mail[k] + ', '
        else:
            email = email + prof_mail[k] 
        k = k + 1
    df.loc[df.index[count], 'Professionals'] = email
    count += 1


df.drop(['emails'], axis = 1, inplace = True)

df.to_csv("prof_3.csv")

