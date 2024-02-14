import axios from 'axios';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT;

export const updateAttendanceRecord = async (uid, attendance) => {
  try {
    const response = await axios.post(`${API_ENDPOINT}`, {
      operation: "update",
      uid,
      attendance
    });
    return response.data.body.response.uid;
  } catch (error) {
    console.error('Error updating attendance record:', error);
    throw error;
  }
};
