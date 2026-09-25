import { SITE } from "@/lib/site";
export const metadata = { title: "Terms and Conditions" };
export default function Page() {
  return (
    <div className="bp-container max-w-3xl py-14">
      <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-700">Legal</p>
      <h1 className="font-display mt-2 text-4xl font-black">Terms & Conditions</h1>
      <div className="prose-bp mt-6 rounded-3xl border bg-white p-6 md:p-10">
        <p>By requesting quotations or purchasing materials from BrickPoint, you agree to the following terms.</p>
        <h2>Quotations & Pricing</h2>
        <ul><li>All prices shared on WhatsApp, phone or this website are quotations valid for the stated period only.</li><li>Material rates may change with market conditions; final rates are confirmed before dispatch.</li><li>Delivery charges (if any) are quoted separately based on site location and quantity.</li></ul>
        <h2>Orders & Payment</h2>
        <ul><li>Orders are confirmed after mutual agreement on rate, quantity and delivery schedule.</li><li>Payment terms are agreed per order. This website has no online checkout or payment gateway.</li></ul>
        <h2>Delivery</h2>
        <ul><li>Delivery timelines are estimated and coordinated per order; they are not guaranteed unless expressly confirmed in writing.</li><li>Customers should ensure site access and unloading arrangements.</li></ul>
        <h2>Quality</h2>
        <ul><li>Natural variation in kiln-fired brick colour is normal.</li><li>Grade and sorting are as described in the quotation; please inspect on delivery and report issues promptly.</li></ul>
        <h2>Content Notice</h2>
        <p>Project visuals labelled “Illustrative construction reference” are inspiration references, not claims of completed supply, unless verified by BrickPoint management.</p>
        <h2>Contact</h2>
        <p>Questions: {SITE.email} • {SITE.phoneDisplay}.</p>
        <p className="text-sm text-[#6b6560]">Last updated: {new Date().getFullYear()}. Editable from the WordPress theme or site admin.</p>
      </div>
    </div>
  );
}
