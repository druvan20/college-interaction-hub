// src/components/EventManagement.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const EventManagement = () => {
  const [events, setEvents] = useState([]);
  const [form, setForm] = useState({
    name: "",
    description: "",
    date: "",
  });

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    const response = await axios.get("/api/events");
    setEvents(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/events", form);
    fetchEvents();
    setForm({ name: "", description: "", date: "" });
  };

  return (
    <div>
      <h1>Event Management</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          value={form.name}
          onChange={handleChange}
          placeholder="Event Name"
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
        <button type="submit">Add Event</button>
      </form>
      <ul>
        {events.map((event) => (
          <li key={event.id}>
            {event.name} - {event.date}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventManagement;
