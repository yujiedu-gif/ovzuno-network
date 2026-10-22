---
title: "Apa Itu Proof of Stake? Cara Validator Mendukung Konsensus Blockchain"
description: "Pelajari apa itu proof of stake, bagaimana stake memengaruhi pemilihan validator, dan bagaimana validator membantu jaringan blockchain mencapai konsensus."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["staking_validators"]
tags: ["apa itu proof stake"]
author: "editorial_team"
primary_keyword: "apa itu proof of stake"
owned_question: "Apa itu proof of stake, dan bagaimana validator menggunakan stake untuk membantu jaringan blockchain mencapai konsensus?"
risk_level: "medium"
---

Proof of stake adalah metode konsensus yang menggunakan kripto yang dikomitmenkan sebagai stake untuk memengaruhi partisipasi atau bobot dalam konsensus. Validator menjalankan tugas yang ditentukan protokol—seperti memeriksa blok, memberikan attestasi, atau mengusulkan blok bila dipilih—agar jaringan dapat menentukan riwayat dan keadaan yang diterima. Mekanisme, pemilihan, dan konsekuensi atas kesalahan berbeda menurut jaringan.

## Apa itu proof of stake dalam blockchain?

Proof of stake (PoS) adalah model konsensus yang menggunakan kripto yang dikunci atau dikomitmenkan sebagai stake; stake memengaruhi bobot peserta dalam konsensus. “Konsensus” di sini berarti proses jaringan untuk menyepakati blok atau riwayat mana yang diterima dan keadaan jaringan yang dihasilkan, sesuai aturan protokol. Stake bukan bukti bahwa semua peserta bertindak benar, dan istilah PoS tidak menjelaskan satu rancangan yang berlaku seragam untuk setiap blockchain. Aturan pemilihan, tugas, kustodi, hadiah, penalti, dan penarikan ditetapkan secara khusus oleh tiap protokol.

Untuk memahami mekanismenya, pisahkan tiga hal: stake sebagai bobot atau komitmen menurut aturan jaringan, validator sebagai peserta dengan tugas protokol, dan konsensus sebagai proses menerima keadaan jaringan. Rincian mekanisme yang disebut di bawah ini bersifat khusus pada protokol terkait, bukan aturan universal.

## Bagaimana stake berhubungan dengan validator?

Validator adalah peserta jaringan yang menjalankan tugas konsensus yang ditentukan protokol. Stake dapat memengaruhi bobot atau peluang partisipasi validator, tetapi cara tepatnya bergantung pada rancangan jaringan. Karena itu, tidak ada satu prosedur seleksi, jumlah minimum, atau pengaturan pendelegasian yang dapat disimpulkan hanya dari istilah “proof of stake.” Untuk menjelaskan sebuah jaringan tertentu, gunakan dokumentasi protokolnya dan identifikasi aturan yang benar-benar berlaku di sana.

Ethereum memberi contoh konkret, bukan definisi bagi semua PoS. Validator Ethereum memeriksa dan memberikan attestasi atas blok, serta mengusulkan blok ketika dipilih oleh protokol. Dalam desain Ethereum, validator menyetor ETH sebagai jaminan ekonomi yang dapat terkena slashing. Itu menjelaskan fungsi komitmen pada jaringan tersebut, tetapi tidak menetapkan persyaratan yang sama untuk jaringan lain.

## Siklus validator: dari pemilihan hingga konsensus

Siklus umum dapat dipahami sebagai rangkaian tugas berikut. Urutan dan istilahnya dapat berbeda antarprotokol; contoh Ethereum di bawah menunjukkan bagaimana beberapa tugas itu diwujudkan pada satu jaringan.

1. **Protokol menentukan peserta yang bertugas.** Aturan jaringan menggunakan stake dalam menentukan bobot partisipasi. Mekanisme pemilihan atau penjadwalan yang sebenarnya merupakan aturan khusus protokol.
2. **Validator yang terpilih dapat mengusulkan blok.** Pada Ethereum, validator mengusulkan blok ketika dipilih. Usulan tersebut menjadi masukan untuk proses pemeriksaan jaringan; pengusulan sendiri tidak berarti blok otomatis diterima.
3. **Validator lain menjalankan tugas pemeriksaan dan attestasi.** Validator Ethereum memeriksa dan memberikan attestasi atas blok. Peran ini berbeda dari mengusulkan blok: attestasi menyampaikan partisipasi validator dalam proses konsensus, bukan membuatnya menjadi pengusul untuk setiap blok.
4. **Protokol menggabungkan masukan peserta untuk menetapkan riwayat.** Ethereum menggabungkan attestasi validator, aturan fork choice, dan finalitas checkpoint berdasarkan kondisi supermayoritas yang ditetapkan protokol. Dengan demikian, blok yang diusulkan, suara atau attestasi peserta, dan keputusan tentang riwayat yang diterima merupakan bagian yang saling berkaitan, tetapi bukan satu tindakan yang sama.

Istilah *finalitas* juga harus dibaca menurut protokol. Dalam Ethereum, suara validator pada blok checkpoint digunakan untuk membedakan riwayat yang telah difinalisasi dari blok yang sekadar telah dimasukkan. Ini adalah ciri desain Ethereum, bukan janji bahwa setiap blok pada setiap jaringan mencapai finalitas dengan cara identik.

## Apa yang terjadi jika validator tidak mengikuti aturan?

Protokol dapat mengaitkan perilaku validator dengan insentif dan konsekuensi. Dalam Ethereum, aturan insentif mencakup hadiah untuk partisipasi yang benar, hadiah yang terlewat atau penalti untuk ketidakaktifan, serta slashing untuk pesan tertentu yang saling bertentangan. Slashing adalah konsekuensi protokol atas tindakan yang ditentukan; pemicu dan akibatnya tidak boleh dianggap sama pada semua jaringan.

Pembedaan ini penting: ketidakaktifan dan pelanggaran tertentu tidak selalu diperlakukan dengan mekanisme yang sama. Jangan mengasumsikan konsekuensi tertentu tanpa memeriksa aturan jaringan yang dibahas. Penjelasan teknis tentang penalti juga tidak membuktikan bahwa validator akan selalu tersedia, bahwa suatu jaringan bebas risiko, atau bahwa partisipasi menghasilkan hasil tertentu.

## Batasan dan hal yang perlu diperiksa

Penjelasan ini menerangkan konsep konsensus, bukan instruksi untuk berpartisipasi, rekomendasi investasi, atau penilaian apakah suatu pilihan sesuai bagi pembaca. Penjelasan ini juga tidak menetapkan apakah staking tersedia atau sah di lokasi mana pun, dan tidak memberi kesimpulan hukum atau pajak. Klaim tentang imbal hasil, biaya, ketersediaan, kepatuhan, kustodi, pemulihan, atau keamanan memerlukan bukti yang sesuai dan terkini; hal-hal tersebut tidak dapat disimpulkan dari uraian umum PoS.

Jika membaca uraian tentang jaringan tertentu, periksa dokumentasi protokol terkini untuk mengetahui bagaimana stake memengaruhi pemilihan, tugas apa yang dilakukan validator, bagaimana blok dan attestasi diperiksa, serta konsekuensi apa yang berlaku untuk ketidakaktifan atau pelanggaran. Jika rincian tersebut tidak dijelaskan oleh sumber yang berwenang, perlakukan sebagai tidak diketahui—bukan sebagai aturan umum semua jaringan proof of stake.

## Sources and references

- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-stake rewards and penalties](https://ethereum.org/developers/docs/consensus-mechanisms/pos/rewards-and-penalties/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-Stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-18.
