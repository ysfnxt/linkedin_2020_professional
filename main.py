import pandas as pd

df = pd.read_csv('file3.csv')
# Converting "emails" column to a list 
email_list = df['emails'].values.tolist()

no_of_emails = []
# Iterate through email_list to append values with type other than "personal"
for i in email_list:
    if "professional"  or "None" in i:
        no_of_emails.append(i.count("professional")+i.count("None"))
    else:
        print('NA')

count = 0
prof_mail = []
# Count no of values apart from "personal"
for i,j in enumerate(email_list):
    b = email_list[i].split(',')
    for i,j in enumerate(b):
        if 'professional' in j or "None" in j:
            prof_mail.append(b[i-1].split(':')[1].replace("'",''))
            count += 1


count = 0
k = 0
for i in no_of_emails:
    # appending values in each row
    email = ''
    for j in range(0,i):
        if i > 1:
            email = email + prof_mail[k] + ', '
        else:
            email = email + prof_mail[k] 
        k = k + 1
    df.loc[df.index[count], 'Professionals'] = email
    count += 1

# Drop "Emails" column 
df.drop(['emails'], axis = 1, inplace = True)

df.to_csv("prof_3.csv")

