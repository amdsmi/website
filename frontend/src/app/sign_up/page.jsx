"use client";

import React, { useEffect, useState } from "react";
import styles from "./signUp.module.css";
import Image from "next/image";
import { useRouter } from "next/navigation";
import {
  getStorage,
  ref,
  uploadBytesResumable,
  getDownloadURL,
} from "firebase/storage";
import { app } from "@/utils/firebase";
import axios from "axios";
const API_URL = "http://127.0.0.1:5000";

const postData = async ( email, name, password, image) => {
  const res = await axios.post(API_URL + "/sign_up", {
    email:email,
    name:name,
    password:password,
    image:image    
  });

  if (!res.status === 200) {
    throw new Error("Faild");
  }

  return res.data;
};

export default function SignUp() {

  const router = useRouter();

  const [propic, setPropic] = useState(null);
  const [media, setMedia] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");

  useEffect(() => {
    const storage = getStorage(app);
    const upload = () => {
      const name = new Date().getTime() + propic.name;
      const storageRef = ref(storage, name);

      const uploadTask = uploadBytesResumable(storageRef, propic);

      uploadTask.on(
        "state_changed",
        (snapshot) => {
          const progress =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          console.log("Upload is " + progress + "% done");
          switch (snapshot.state) {
            case "paused":
              console.log("Upload is paused");
              break;
            case "running":
              console.log("Upload is running");
              break;
          }
        },
        (error) => {},
        () => {
          getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
            setMedia(downloadURL);
          });
        }
      );
    };

    propic && upload();
  }, [propic]);

    const handleSubmit = async () => {
      if (password === confirm){
        const resp = await postData(email,username, password, media);
        if (resp.status === "ok"){
          router.push('/login')
        }
      }else{
        throw new Error("your passwords are not match");
      }
    };

  return (
    <div className={styles.container}>
      <div className={styles.wrapper}>
        <input
          className={styles.input}
          type="file"
          id="image"
          onChange={(e) => setPropic(e.target.files[0])}
        />
        <label htmlFor="image">
          <Image
            className={styles.image}
            src={propic ? URL.createObjectURL(propic) : "/user_image.svg"}
            alt="google"
            width={200}
            height={200}
          />
        </label>
        <Image
          className={styles.smile}
          src="/smile.png"
          alt="google"
          width={150}
          height={150}
        />
        <input
          className={styles.socialButton}
          type="username"
          placeholder="User name"
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          className={styles.socialButton}
          type="email"
          placeholder="example@gmail.com"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className={styles.socialButton}
          type="password"
          placeholder="Password..."
          onChange={(e) => setPassword(e.target.value)}
        />
        <input
          className={styles.socialButton}
          type="password"
          placeholder="Confirm Password..."
          onChange={(e) => setConfirm(e.target.value)}
        />
        <button className={styles.socialButton} onClick={() => handleSubmit()}>
          Submit
        </button>
      </div>
    </div>
  );
}