import React from "react";
import styles from "./menu.module.css";
import MenuPosts from "../menu_posts/MenuPosts";
import MenuCategories from "../menu_categories/MenuCategories";

export default function Menu() {
  return (
    <div className={styles.container}>
      <h2 className={styles.subtitle}>{"what's hot "}</h2>
      <h1>Most Popular</h1>
      <MenuPosts withImage={true} />

      <h2 className={styles.subtitle}>Who am I</h2>
      <h1 className={styles.categoriesTitle}>My Jurny</h1>
      <MenuCategories />

      <h2 className={styles.subtitle}>Chosen by Editors</h2>
      <h1>Editor Pick</h1>
      <MenuPosts withImage={false} />
    </div>
  );
}
