/* eslint-disable */
export default function updateStudentGradeByCity(students, city, newGrades) {
    const studentByCity = students
      .filter((student) => student.location === city)
      .map(student => {
        const homework = newGrades.find(grade => grade.studentId === student.id);
        if (homework) {
          student.grade = homework.grade;
        } else {
          student.grade = 'N/A';
        }
        return student;
      });
    return studentByCity;
  }
  