// src/components/StudentProfile.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const StudentProfile = () => {
  const [students, setStudents] = useState([]);
  const [form, setForm] = useState({
    name: "",
    email: "",
    enrollment_no: "",
    department: "",
    year: "",
  });

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    const response = await axios.get("/api/students");
    setStudents(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/students", form);
    fetchStudents();
    setForm({
      name: "",
      email: "",
      enrollment_no: "",
      department: "",
      year: "",
    });
  };

  return (
    <div>
      <h1>Student Profile</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          value={form.name}
          onChange={handleChange}
          placeholder="Name"
          required
        />
        <input
          name="email"
          value={form.email}
          onChange={handleChange}
          placeholder="Email"
          required
        />
        <input
          name="enrollment_no"
          value={form.enrollment_no}
          onChange={handleChange}
          placeholder="Enrollment No"
          required
        />
        <input
          name="department"
          value={form.department}
          onChange={handleChange}
          placeholder="Department"
          required
        />
        <input
          name="year"
          value={form.year}
          onChange={handleChange}
          placeholder="Year"
          required
        />
        <button type="submit">Add Student</button>
      </form>
      <ul>
        {students.map((student) => (
          <li key={student.id}>
            {student.name} - {student.department}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default StudentProfile;
