"use client";

import api from "@/lib/api";

interface Props {
  onUploadSuccess: () => void;
}

export default function UploadButton({
  onUploadSuccess,
}: Props) {

  async function uploadFile(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    const file = event.target.files?.[0];

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {
      await api.post(
        "/documents/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      alert("Document uploaded!");

      onUploadSuccess();

    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  }

  return (
    <label className="mb-5 block cursor-pointer rounded-lg bg-blue-600 py-3 text-center text-white hover:bg-blue-700">
      + Upload PDF

      <input
        type="file"
        accept=".pdf"
        hidden
        onChange={uploadFile}
      />
    </label>
  );
}