// src/components/PlacementHub.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const PlacementHub = () => {
  const [placements, setPlacements] = useState([]);
  const [form, setForm] = useState({
    company: "",
    position: "",
    description: "",
    date: "",
  });

  useEffect(() => {
    fetchPlacements();
  }, []);

  const fetchPlacements = async () => {
    const response = await axios.get("/api/placements");
    setPlacements(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/placements", form);
    fetchPlacements();
    setForm({ company: "", position: "", description: "", date: "" });
  };

  return (
    <div>
      <h1>Placement Hub</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="company"
          value={form.company}
          onChange={handleChange}
          placeholder="Company"
          required
        />
        <input
          name="position"
          value={form.position}
          onChange={handleChange}
          placeholder="Position"
          required
        />
        <textarea
          name="description"
          value={form.description}
          onChange={handleChange}
          placeholder="Description"
          required
        ></textarea>
        <input
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
          required
        />
        <button type="submit">Add Placement</button>
      </form>
      <ul>
        {placements.map((placement) => (
          <li key={placement.id}>
            {placement.company} - {placement.position}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PlacementHub;
