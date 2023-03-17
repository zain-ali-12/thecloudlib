def update_qualifications(app, db):
    from .models import Qualification
    quals = ['IGCSE', "AS-Level", "A-Level"]
    with app.app_context():
        for i in quals:
            db.session.add(Qualification(id=i))
            db.session.commit()


def update_subjects(app, db):
    from .models import Subject, Qualification
    with open('subs.csv', 'r') as f:
        csv_data = [data[:-1] for data in f.readlines()][1:]
        for data in csv_data:
            subject_id, subject_name, qualification = data.split(",")
            new_subject = Subject(id=subject_id, subject_name=subject_name)
            # with app.app_context():
            db.session.add(new_subject)
            db.session.commit()
            for qual in qualification.split(" "):
                new_subject.qualifications.append(Qualification.query.filter_by(id=qual).first())
                db.session.commit()