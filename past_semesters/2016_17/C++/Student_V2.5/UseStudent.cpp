#include "Student.h"

//friend function
void DisplayStudent(Student& s) {
	cout << setw(15) << s.name //s. is an object reference -- friend function obviates 'get'
		<< setw(10) << s.midTerm
		<< setw(10) << s.finalExam
		<< setw(10) << fixed << setprecision(3) 
		<< s.getAverage() << endl;
}
istream& operator >> (istream& lhs, Student& rhs) {
	lhs >> rhs.name >> rhs.midTerm >> rhs.finalExam;
	return lhs;
}
//free function
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

// > operator overloading as free function
// return type is bool -- comparison of student points totals
bool operator > (Student& rhs, Student& lhs) {
	return rhs.getTtlPoints() > lhs.getTtlPoints();
}

int main() {
	cout << "Number of student objects is " << Student::getNumObj() << endl;
	Student st1("Larry", 75, 80), st2("Curly", 80, 90), st3;
	//compare students
	if (st1 > st2) {
		cout << st1.getName() << " has more points than " << st2.getName() << endl;
		st3 = st1;
	}
	else {
		cout << st1.getName() << " has fewer or as many points as " 
			<< st2.getName() << endl;
		st3 = st2;
	}
	//to change the name on the grade info, access setName function
	DisplayStudent(st3);
	cout << "**MOE: woah woah woah, lemme put MY name on this...\n";
	st3.setName("moe");
	cout << "Moe's Information: \n";
	DisplayStudent(st3);
	cout << "Please input moe's real midterm and final: ";
	cin >> st3;
	cout << "Moe's TRUE Information: \n";
	DisplayStudent(st3);
	cout << "Number of student objects is " << Student::getNumObj() << endl;
	return 0;
}