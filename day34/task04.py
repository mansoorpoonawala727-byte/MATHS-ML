p_spam = 0.3
p_not_spam = 0.7
p_free_given_spam = 0.8
p_free_given_not_spam = 0.1

def bayes_spam(p_spam, p_free_given_spam,
               p_not_spam, p_free_given_not_spam):
    num = p_free_given_spam*p_spam
    no = p_free_given_not_spam*p_not_spam
    denom = num + no
    p_spam_given_free = num/denom
    return p_spam_given_free
result=bayes_spam(p_spam, p_free_given_spam, p_not_spam, p_free_given_not_spam)
print("Prior Spam Probability:",p_spam)
print("Probability of 'FREE' if Spam:",p_free_given_spam*p_spam)
print("Probability of 'FREE' if Not Spam:",p_free_given_not_spam*p_not_spam)
print(f"Posterior Spam Probability:{result:.2%}")
choice = input("Does the email contain 'FREE'? (yes/no): ").lower()
if choice=="yes":
    print(f"Posterior Spam Probability: {result:.2%}")
    if result>0.7:
       print("⚠️ Likely Spam")
    else:
       print("✅ Probably Legitimate")     
else:
    print("""No evidence received.
Spam probability remains the prior probability: 0.3
          ✅ Probably Legitimate
          
""")   
    