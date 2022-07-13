import Head from "next/head";
import Image from "next/image";
import styles from "../styles/Home.module.css";
import { Button, Card, CardGroup, Col, Container, Row } from "react-bootstrap";

const Home = (props) => {
  return (
    <div className={styles.container}>
      <Head>
        <title> PostPaste </title>{" "}
        <meta
          name="description"
          content="A social media service to learn full stack development"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>{" "}
      <main className={styles.main}>
        <h1 className={styles.title}> PostPaste </h1>{" "}
        <p className={styles.description}>
          A social media service to learn full stack development
        </p>{" "}
        <CardGroup className="rowwise">
          {props.posts.map((post) => (
            <Card>
              <Card.Header>
                #{post.id} from user {post.user_id}{" "}
              </Card.Header>
              <Card.Body>
                <Card.Text>{post.content}</Card.Text>
              </Card.Body>
            </Card>
          ))}
        </CardGroup>
      </main>{" "}
      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{" "}
          <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16} />{" "}
          </span>{" "}
        </a>{" "}
      </footer>{" "}
    </div>
  );
};

export async function getStaticProps() {
  const res = await fetch("http://backend/posts");
  const posts = await res.json();

  return {
    props: {
      posts,
    },
  };
}

export default Home;
