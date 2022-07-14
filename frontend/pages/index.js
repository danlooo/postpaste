import { Card, CardGroup } from "react-bootstrap";

function Home({ posts }) {
  return (
    <>
      <h1>PostPaste</h1>
      <CardGroup className="rowwise flex-column">
        {posts.map((post) => {
          return (
            <Card>
              <Card.Title>Post {post.id}</Card.Title>
              <Card.Body>{post.content}</Card.Body>
            </Card>
          );
        })}
      </CardGroup>
    </>
  );
}
export default Home;

export async function getServerSideProps() {
  const res = await fetch("http://backend/posts");
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}
