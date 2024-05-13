import React, { useEffect, useState } from "react";
import { Box } from "@mui/material";
import PostsTable from "../../components/postsTable";

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/posts")
      .then((response) => response.json())
      .then((json) => {
        setPosts(json);
      });
  }, []);

  return (
    <Box m="20px">
      <PostsTable posts={posts} />
    </Box>
  );
};

export default Posts;
