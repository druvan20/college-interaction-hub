// src/components/FeedbackRatings.js
import React, { useState, useEffect } from "react";
import axios from "axios";

const FeedbackRatings = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  const [form, setForm] = useState({
    user_id: "",
    content: "",
    rating: "",
    date: "",
  });

  useEffect(() => {
    fetchFeedbacks();
  }, []);

  const fetchFeedbacks = async () => {
    const response = await axios.get("/api/feedbacks");
    setFeedbacks(response.data);
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("/api/feedbacks", form);
    fetchFeedbacks();
    setForm({ user_id: "", content: "", rating: "", date: "" });
  };

  return (
    <div>
      <h1>Feedback & Ratings</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="user_id"
          value={form.user_id}
          onChange={handleChange}
          placeholder="User ID"
          required
        />
        <textarea
          name="content"
          value={form.content}
          onChange={handleChange}
          placeholder="Feedback Content"
          required
        ></textarea>
        <input
          name="rating"
          type="number"
          min="1"
          max="5"
          value={form.rating}
          onChange={handleChange}
          placeholder="Rating"
          required
        />
        <input
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
          required
        />
        <button type="submit">Submit Feedback</button>
      </form>
      <ul>
        {feedbacks.map((feedback) => (
          <li key={feedback.id}>
            {feedback.content} - {feedback.rating}/5
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FeedbackRatings;
