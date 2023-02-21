def getSpamEmails(subjects, spam_words):
    '''
        email is spam if it contains at least 2 spam words in subject
        repeat spam words are still counted, so if spam word reapeats twice then it is spam
        spam words are not case-sensitive


        return array of n strings ("spam" or "not_spam")

        BRUTE FORCE
            iterate through array
                for each subject. split the subject to array of words
                iterate through array of words and if have 2 spam words then append spam to result array
                if dont have 2 spam words then append not_spam to result array

            return result array
    '''
    res = []
    spam_words_set = set([ word.upper() for word in spam_words ])
    for subject in subjects:
        words = subject.split(' ')
        count = 0
        for word in words:
            if word.upper() in spam_words_set:
                count += 1
            if count == 2:
                res.append('spam')
                break
        if count < 2:
            res.append('not_spam')
    return res
