import axios from 'axios';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT;

export const insertAttendanceRecord = async (name, email, attendance, date) => {
  try {
    const response = await axios.post(`${API_ENDPOINT}`, {
      operation: "insert",
      name,
      email,
      attendance,
      date
    });
    return response.data.body.response.uid;
  } catch (error) {
    console.error('Error inserting attendance record:', error);
    throw error;
  }
};
