import csv

with open('books.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    sum_score = {}
    count_scores = {}
    for row in reader:
        if 'Сюзанна Коллинз' in row['Name']:
            print(f'Голодные игры : {row["score"]},  - {row["titleProject_id"]}')

        sum_score[row['class']] = sum_score.get(row['class'], 0) + (int(row['score']) if row['score'] != 'None' else 0)
        count_scores[row['class']] = count_scores.get(row['class'], 0) + 1

    for row in reader:
        if row['score'] == 'None':
            row['score'] = round(sum_score[row['class']] / count_scores[row['class']], 3)

with open('books.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(reader)