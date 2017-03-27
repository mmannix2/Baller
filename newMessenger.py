import smtplib
import psycopg2
import psycopg2.extras
import time
import sys

lastGameIdSent=0

gmail_user = None
gmail_password = None

def main(args):
    #reminders?
    
    #parse args for gmail login info
    if len(args) != 3:
        #Not enough arguments
        print 'Usage %s gmail_user gmail_password' % args[0]
        return -1
    else:
        gmail_user = args[1]
        gmail_password = args[2]

    while(True):
        findPlayers()
        time.sleep(300)

def findPlayers():
    cur = connectToDB()
    query = 'SELECT COUNT(id) FROM games;'
    try:
        cur.execute(query)
        totGames=cur.fetchOne()
        print totGames
        while (lastGameIdSent<totGames):
            lastGameIdSent+=lastGameIdSent()
            queryA='SELECT address FROM games WHERE id=%s'%lastGameIdSent
            queryC='SELECT city FROM games WHERE id=%s'%lastGameIdSent
            queryS='SELECT state FROM games WHERE id=%s'%lastGameIdSent
            queryZ='SELECT zip FROM games WHERE id=%s'%lastGameIdSent
            queryF='SElECT fun FROM games WHERE id=%s'%lastGameIdSent
            queryI='SELECT intense FROM games WHERE id=%s'%lastGameIdSent
            queryH='SELECT hardcore FROM games WHERE id=%s'%lastGameIdSent
            queryD='SELECT day FROM games WHERE id=%s'%lastGameIdSent
            queryT='SELECT day FROM games WHERE id=%s'%lastGameIdSent

            cur.execute(queryA)
            gameA=cur.fetchOne()
            cur.execute(queryC)
            gameC=cur.fetchOne()
            cur.execute(queryS)
            gameS=cur.fetchOne()
            cur.execute(queryZ)
            gameZ=cur.fetchOne()
            cur.execute(queryF)
            gameF=cur.fetchOne()
            cur.execute(queryI)
            gameI=cur.fetchOne()
            cur.execute(queryH)
            gameH=cur.fetchOne()
            cur.execute(queryD)
            gameD=cur.fetchOne()
            cur.execute(queryT)
            gameT=cur.fetchOne()
            

            #player info
            pQuery='SELECT phone FROM players;'
            cur.execute(pcQuery);
            pCount=cur.fetchAll()
            for p in pCount:
                pqueryZ='SELECT zipcode FROM players WHERE phone=%s'%p
                pqueryZR='SELECT ziprange FROM players WHERE phone=%s'%p
                pqueryF='SELECT fun FROM players WHERE phone=%s'%p
                pqueryI='SELECT intense FROM players WHERE phone=%s'%p
                pqueryH='SELCT hardcore FROM players WHERE phone=%s'%p

                cur.execute(pqueryZ)
                playerZ=cur.fetchOne()
                cur.execute(pqueryZR)
                playerZR=cur.fetchOne()
                cur.execute(pqueryF)
                playerF=cur.fetchOne()
                cur.execute(pqueryI)
                playerI=cur.fetchOne
                cur.executre(pqueryH)
                playerH=cur.fetchOne()

                if(gameZ in range((playerZ-playerZR),(playerZ+playerZR))):
                    if((gameF==playerF) or (gameI==playerI) or (gameH==playerH)):
                        #game on!!!
                        sendMessage(p, gameA, gameC, gameS, gameZ, gameD, gameT)
    except Exception as e:
        print e

def connectToDB():
    connectionString= 'dbname=basket user=postgres password=hackUVA host=localhost'
    try:
        print("Connected to the Database!")
        return psychopg2.connect(connectString)
    except:
        print("JK! Can't connect to the database!")

def sendMessage(phone, a, c, s, z, d, t):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user,gmail_password)
        print "logged in"
        sentFrom = gmail_user
    #    to=['7034899030@messaging.sprintpcs.com', '7037275554@vtext.com']
        to=['%s@messaging.sprintpcs.com'%phone , '%s@tmomaol.net'%phone , '%s@txt.att.net'%phone , '%s@vtext.com'%phone]
        subject=''
        body='''GAME ALERT!\n%s\n%s\n%s\n%s\non:\n%s\n%s'''%(a,c,s,z,d,t)

        emailText = """\
                    From: %s
                    To: %s
                    Subject: %s

                    %s
                    """%(sentFrom, ", ".join(to), subject, body)
        while(True):
            server.sendmail(sentFrom, to, emailText)
            print "sent"
        server.close()

    except Exception as e:
        print e



if __name__ == '__main__':
    main(sys.argv)
