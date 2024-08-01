// src/components/ParentPortal.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const ParentPortal = () => {
  const [parents, setParents] = useState([]);
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    student_id: "",
  });

  useEffect(() => {
    fetchParents();
  }, []);

  const fetchParents = async () => {
    const response = await axios.get("/api/parents");
    setParents(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/parents", form);
    fetchParents();
    setForm({ name: "", email: "", phone: "", student_id: "" });
  };

  return (
    <div>
      <h1>Parent Portal</h1>
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
          name="phone"
          value={form.phone}
          onChange={handleChange}
          placeholder="Phone"
          required
        />
        <input
          name="student_id"
          value={form.student_id}
          onChange={handleChange}
          placeholder="Student ID"
          required
        />
        <button type="submit">Add Parent</button>
      </form>
      <ul>
        {parents.map((parent) => (
          <li key={parent.id}>
            {parent.name} - {parent.email}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ParentPortal;
