import styles from "./homepage.module.css";
import Featured from "@/components/featured/Featured";
import CategoryList from "@/components/category_list/CategoryList";
import CardList from "@/components/card_list/CardList";
import Menu from "@/components/Menu/Menu";

export default function Home({searchParams}) {
  const pageNum= parseInt(searchParams.page) || 1
  return (
    <div className={styles.container}>
      <Featured />
      <CategoryList />
      <div className={styles.content}>
        <CardList pageNum={pageNum}/>
        <Menu />
      </div>
    </div>
  );
}
