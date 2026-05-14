import React, { useEffect, useState } from "react";
import axios from "axios";

const Account = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true); // Optional loading state
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch all users
    const fetchUsers = async () => {
      try {
        const res = await axios.get("http://localhost:5000/api/auth/users");
        setUsers(res.data);
        console.log(res.data)
      } catch (err) {
        setError(err.response?.data?.error || "Failed to fetch users");
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">User Accounts</h2>

      {loading && <p>Loading users...</p>}
      {error && <p className="text-danger">{error}</p>}

      {!loading && users.length === 0 && <p>No users found.</p>}

      {!loading && users.length > 0 && (
        <table className="table table-bordered">
          <thead className="table-light">
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Password</th>
              {/* Add more fields if needed */}
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user._id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.password}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Account;
