import torch
import sys
import argparse
from pathlib import Path
from lama_inpaint import inpaint_img_with_lama
from saicinpainting.utils import load_img_to_array, save_array_to_img, dilate_mask


def setup_args(parser):
    parser.add_argument(
        "--input_img", type=str, required=True,
        help="Path to a single input img",
    )
    parser.add_argument(
        "--input_mask", type=str, required=True,
        help="Path to a single input mask",
    )
    parser.add_argument(
        "--dilate_kernel_size", type=int, default=None,
        help="Dilate kernel size. Default: None",
    )
    parser.add_argument(
        "--output_dir", type=str, required=True,
        help="Output path to the directory with results.",
    )
    parser.add_argument(
        "--lama_config", type=str,
        default="./lama/configs/prediction/default.yaml",
        help="The path to the config file of lama model. "
             "Default: the config of big-lama",
    )
    parser.add_argument(
        "--lama_ckpt", type=str, required=True,
        help="The path to the lama checkpoint.",
    )


if __name__ == "__main__":
    """Example usage:
    python remove_anything.py \
        --input_img FA_demo/FA1_dog.png \
        --coords_type key_in \
        --point_coords 750 500 \
        --point_labels 1 \
        --dilate_kernel_size 15 \
        --output_dir ./results \
        --sam_model_type "vit_h" \
        --sam_ckpt sam_vit_h_4b8939.pth \
        --lama_config lama/configs/prediction/default.yaml \
        --lama_ckpt big-lama
    """
    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])
    device = "cuda" if torch.cuda.is_available() else "cpu"

    img = load_img_to_array(args.input_img)
    mask = load_img_to_array(args.input_mask)

    # dilate mask to avoid unmasked edge effect
    mask = dilate_mask(mask, args.dilate_kernel_size)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    img_inpainted_p = out_dir / f"{Path(args.input_mask).stem}_background.png"
    img_inpainted = inpaint_img_with_lama(
        img, mask, args.lama_config, args.lama_ckpt, device=device)
    save_array_to_img(img_inpainted, img_inpainted_p)