import axios from 'axios';

const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT;

export const deleteAttendanceRecord = async (uid) => {
  try {
    const response = await axios.post(`${API_ENDPOINT}`, {
      operation: "delete",
      uid
    });
    return response.data.body.response.uid;
  } catch (error) {
    console.error('Error deleting attendance record:', error);
    throw error;
  }
};
