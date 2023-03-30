from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for itme in question_data:
    question_text = itme["text"]
    question_answer = itme["answer"]
# 把question_data里的数据传输到question_text和question_answer里
    new_question = Question(question_text, question_answer)
# 创立一个新的object叫new_question，然后把上面的两个变量传输到Question的class里
# 这里的question class的意义是，当很多object要被创立，那么如果会写很多行代码，如果有一个question的class那么我们就可以直接写
# new_question = Question(question_text, question_answer)，new_question_2 = Question(question_text, question_answer)
# 而不是new_question = Question，new_question.id = "001"，new_question.name = "jack"
# new_question_2 = Question，new_question_2.id = "002"，new_question_2.name = "veronica"
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz.next_question()

