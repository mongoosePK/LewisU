//William Pulkownik
// 20APR2016

#include "Student.h"


void displayStudent(Student& s) {
	cout << setw(15) << s.getName()
		<< setw(10) << s.getMidTerm()
		<< setw(10) << s.getFinalExam()
		<< setw(10) << fixed << setprecision(3)
		<< s.getAverage() << endl;
}

Student getStudent() {
	string name;
	int mt, fnl;
	Student st;
	cout << "\nInput first name: ";
	cin >> name;
	st.setName(name);
	cout << "Mid term score: ";
	cin >> mt;
	st.setMidTerm(mt);
	cout << "Final exam score: ";
	cin >> fnl;
	st.setFinalExam(fnl);
	return st;
}

int main() {
	//initialize with constructor
	Student st1("Larry", 75, 90), st2 = getStudent();
	
	displayStudent(st1);
	displayStudent(st2);
	//using ARRAYS
	Student stArr[3] = {Student(), Student("Moe", 80, 95)};
	displayStudent(stArr[1]);

	return 0;
}