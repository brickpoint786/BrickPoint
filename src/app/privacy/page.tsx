import { SITE } from "@/lib/site";
export const metadata = { title: "Privacy Policy" };
export default function Page() {
  return (
    <div className="bp-container max-w-3xl py-14">
      <p className="text-xs font-black uppercase tracking-[0.22em] text-orange-700">Legal</p>
      <h1 className="font-display mt-2 text-4xl font-black">Privacy Policy</h1>
      <div className="prose-bp mt-6 rounded-3xl border bg-white p-6 md:p-10">
        <p>BrickPoint respects your privacy. This policy explains what information we collect through quotation forms, WhatsApp inquiries and website usage — and how we use it.</p>
        <h2>Information We Collect</h2>
        <ul><li>Contact details you provide (name, phone, email, company, site location).</li><li>Quotation details (materials, quantities, messages).</li><li>Basic website analytics (pages visited, device type).</li></ul>
        <h2>How We Use It</h2>
        <ul><li>To prepare quotations and coordinate deliveries.</li><li>To respond to inquiries via phone, WhatsApp or email.</li><li>To improve our catalogue and customer experience.</li></ul>
        <h2>Sharing</h2>
        <p>We do not sell your personal data. Information is shared only with staff and delivery partners as needed to fulfil your request, or when required by law.</p>
        <h2>WhatsApp Communication</h2>
        <p>By contacting {SITE.phoneDisplay} on WhatsApp you consent to receiving quotation and order-related messages from BrickPoint.</p>
        <h2>Contact</h2>
        <p>For privacy questions contact {SITE.email} or {SITE.phoneDisplay}.</p>
        <p className="text-sm text-[#6b6560]">Last updated: {new Date().getFullYear()}. Editable from the WordPress theme or site admin.</p>
      </div>
    </div>
  );
}
