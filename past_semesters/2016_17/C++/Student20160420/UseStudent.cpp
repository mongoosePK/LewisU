#include "Student.h"

void DisplayStudent(Student& s) {
	//cout << setw(15) << s.getName()
	cout << setw(15) << s.name
		//<< setw(10) << s.getMidTerm()
		<< setw(10) << s.midTerm
		//<< setw(10) << s.getFinalExam()
		<< setw(10) << s.finalExam
		<< setw(10) << fixed << setprecision(3) 		
		//<< s.getAverage() << endl;
		<< s.getAverage() << endl;
}

Student GetStudent() {
	Student st;
	string name;
	int mt, fnl;
	cout << "\nInput first name: ";
	cin >> name;
	st.setName(name);
	cout << "MidTerm score: ";
	cin >> mt;
	st.setMidTerm(mt);
	cout << "Final score: ";
	cin >> fnl;
	st.setFinalExam(fnl);
	return st;
}

int main() {
	cout << "number of student objects is " << Student::getNumObj() << endl;
	Student st1("Larry", 75, 90), st2 = GetStudent();
	// st2 = GetStudent();
	DisplayStudent(st1);
	DisplayStudent(st2);
	cout << "number of student objects is " << st1.getNumObj() << endl;
	// using arrays
	Student stArr[3] = {Student(), Student("Moe", 80, 95)};
	DisplayStudent(stArr[1]);
	cout << "number of student objects is " << stArr[2].getNumObj() << endl;
	return 0;
}