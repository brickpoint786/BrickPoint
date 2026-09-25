import {
  pgTable,
  serial,
  varchar,
  text,
  integer,
  boolean,
  timestamp,
  jsonb,
} from "drizzle-orm/pg-core";

// ---------- Product Categories (bp_product_category) ----------
export const productCategories = pgTable("product_categories", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 160 }).notNull(),
  slug: varchar("slug", { length: 160 }).notNull().unique(),
  description: text("description"),
  image: text("image"),
  icon: varchar("icon", { length: 80 }),
  banner: text("banner"),
  featuredVideo: text("featured_video"),
  whatsappMessage: text("whatsapp_message"),
  sortOrder: integer("sort_order").default(0),
  createdAt: timestamp("created_at").defaultNow(),
});

export type ProductCategory = typeof productCategories.$inferSelect;
export type NewProductCategory = typeof productCategories.$inferInsert;

// ---------- Products (bp_product) ----------
export const products = pgTable("products", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 200 }).notNull(),
  slug: varchar("slug", { length: 200 }).notNull().unique(),
  categoryId: integer("category_id"),
  featuredImage: text("featured_image"),
  gallery: jsonb("gallery").$type<string[]>().default([]),
  shortDescription: text("short_description"),
  fullDescription: text("full_description"),
  price: varchar("price", { length: 60 }),
  priceLabel: varchar("price_label", { length: 120 }),
  unit: varchar("unit", { length: 60 }),
  availability: varchar("availability", { length: 60 }).default("In Stock"),
  badge: varchar("badge", { length: 80 }),
  specifications: jsonb("specifications").$type<{ label: string; value: string }[]>().default([]),
  features: jsonb("features").$type<string[]>().default([]),
  sku: varchar("sku", { length: 80 }),
  featured: boolean("featured").default(false),
  videoUrl: text("video_url"),
  videoType: varchar("video_type", { length: 20 }).default("mp4"),
  brochureUrl: text("brochure_url"),
  whatsappMessage: text("whatsapp_message"),
  relatedIds: jsonb("related_ids").$type<number[]>().default([]),
  sortOrder: integer("sort_order").default(0),
  createdAt: timestamp("created_at").defaultNow(),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export type Product = typeof products.$inferSelect;
export type NewProduct = typeof products.$inferInsert;

// ---------- Video Categories (bp_video_category) ----------
export const videoCategories = pgTable("video_categories", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 160 }).notNull(),
  slug: varchar("slug", { length: 160 }).notNull().unique(),
  description: text("description"),
  image: text("image"),
  sortOrder: integer("sort_order").default(0),
});

export type VideoCategory = typeof videoCategories.$inferSelect;

// ---------- Videos (bp_video) ----------
export const videos = pgTable("videos", {
  id: serial("id").primaryKey(),
  title: varchar("title", { length: 220 }).notNull(),
  slug: varchar("slug", { length: 220 }).notNull().unique(),
  description: text("description"),
  categoryId: integer("category_id"),
  thumbnail: text("thumbnail"),
  sourceType: varchar("source_type", { length: 20 }).default("mp4"),
  videoUrl: text("video_url"),
  fileUrl: text("file_url"),
  duration: varchar("duration", { length: 20 }),
  featured: boolean("featured").default(false),
  displayOrder: integer("display_order").default(0),
  relatedProducts: jsonb("related_products").$type<number[]>().default([]),
  relatedProjects: jsonb("related_projects").$type<number[]>().default([]),
  relatedLocations: jsonb("related_locations").$type<number[]>().default([]),
  captionsUrl: text("captions_url"),
  publishedAt: timestamp("published_at").defaultNow(),
});

export type Video = typeof videos.$inferSelect;

// ---------- Projects ----------
export const projects = pgTable("projects", {
  id: serial("id").primaryKey(),
  title: varchar("title", { length: 220 }).notNull(),
  slug: varchar("slug", { length: 220 }).notNull().unique(),
  category: varchar("category", { length: 120 }),
  location: varchar("location", { length: 160 }),
  description: text("description"),
  featuredImage: text("featured_image"),
  gallery: jsonb("gallery").$type<string[]>().default([]),
  videoUrl: text("video_url"),
  status: varchar("status", { length: 80 }).default("Illustrative construction reference"),
  relatedProducts: jsonb("related_products").$type<number[]>().default([]),
  featured: boolean("featured").default(false),
  illustrative: boolean("illustrative").default(true),
  sortOrder: integer("sort_order").default(0),
});

export type Project = typeof projects.$inferSelect;

// ---------- Locations (Bhattas / Office) ----------
export const locations = pgTable("locations", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 220 }).notNull(),
  slug: varchar("slug", { length: 220 }).notNull().unique(),
  address: text("address"),
  description: text("description"),
  image: text("image"),
  mapsUrl: text("maps_url"),
  phone: varchar("phone", { length: 40 }),
  hours: varchar("hours", { length: 120 }),
  videoUrl: text("video_url"),
  sortOrder: integer("sort_order").default(0),
});

export type Location = typeof locations.$inferSelect;

// ---------- Blog posts ----------
export const posts = pgTable("posts", {
  id: serial("id").primaryKey(),
  title: varchar("title", { length: 240 }).notNull(),
  slug: varchar("slug", { length: 240 }).notNull().unique(),
  excerpt: text("excerpt"),
  content: text("content"),
  featuredImage: text("featured_image"),
  category: varchar("category", { length: 120 }),
  tags: jsonb("tags").$type<string[]>().default([]),
  author: varchar("author", { length: 120 }).default("BrickPoint Team"),
  publishedAt: timestamp("published_at").defaultNow(),
});

export type Post = typeof posts.$inferSelect;

// ---------- Inquiries / Contact ----------
export const inquiries = pgTable("inquiries", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 160 }).notNull(),
  phone: varchar("phone", { length: 40 }).notNull(),
  email: varchar("email", { length: 160 }),
  company: varchar("company", { length: 160 }),
  material: varchar("material", { length: 160 }),
  quantity: varchar("quantity", { length: 120 }),
  location: varchar("location", { length: 160 }),
  message: text("message"),
  productId: integer("product_id"),
  createdAt: timestamp("created_at").defaultNow(),
});

export type Inquiry = typeof inquiries.$inferSelect;

// ---------- Theme settings (key/value) ----------
export const settings = pgTable("settings", {
  key: varchar("key", { length: 120 }).primaryKey(),
  value: text("value"),
  updatedAt: timestamp("updated_at").defaultNow(),
});

export type Setting = typeof settings.$inferSelect;
